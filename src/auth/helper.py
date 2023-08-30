from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import bcrypt
import pymysql
from dotenv import load_dotenv
import os
from pathlib import Path




##password functions
def hash_password(plain_password):
    """Hash a password for storing."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(plain_password.encode('utf-8'), salt)
def verify_password(stored_password, provided_password):
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('utf-8'))

def set_style(window):
    style = ttk.Style(window)  # Create an instance of ttk.Style
    window.tk.call("source", "../theme/forest-light.tcl")
    window.tk.call("source", "../theme/forest-dark.tcl")
    style.theme_use("forest-dark")


    #icon for the window tab
    ico = Image.open('../image/Z.png')
    icon = ImageTk.PhotoImage(ico)
    window.wm_iconphoto(False, icon)

    global userImage, usernameImage, lockImage
    userImage=PhotoImage(file='../image/logo.png')
    usernameImage=PhotoImage(file='../image/user.png')
    lockImage=PhotoImage(file='../image/lock.png')

def load_env_vars():
    # Specify the path to the .env file
    env_path = Path('.') / 'key' / '.env'
    
    # Load the .env file
    load_dotenv(dotenv_path=env_path)
    
    # Now set the global variables
    global hosts, u, us, passwords, databases
    hosts = os.environ.get('DB_HOST')
    u = os.environ.get('DB_USER')
    us = os.environ.get('DB_USERS')
    passwords = os.environ.get('DB_PASS')
    databases = os.environ.get('DB_NAME')
    
    # Verify that all variables were set
    if any(var is None for var in [hosts, u, us, passwords, databases]):
        raise EnvironmentError("Could not load all required environment variables.")


def verify_login(username, password):
    mycursor = None
    con = None
    try:
        con = pymysql.connect(host=hosts, user=u, password=passwords, database=databases)
        mycursor = con.cursor()

        # Using parameterized query to prevent SQL injection
        sql = (f"SELECT password_hash FROM {us} WHERE username = %s")
        mycursor.execute(sql, (username,))
        result = mycursor.fetchone()
        
        if result and verify_password(result[0], password):
            return True
        else:
            return False
            
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        # Close cursor and connection
        mycursor.close()
        con.close()



def new_user(userEntry, passEntry, emailEntry, entryScreen, window):
    pas = hash_password(passEntry.get())
    con = pymysql.connect(host=hosts, user=u, password=passwords, database=databases)
    mycursor = con.cursor()
    check_username = (f"SELECT * FROM {us} WHERE username=%s")
    mycursor.execute(check_username, (userEntry.get()))
    result = mycursor.fetchall()
    

    if not result:
        query = (f"INSERT INTO {us} (username, password_hash, email) " \
                            "VALUES (%s, %s, %s)")
        values = (userEntry.get(), pas, emailEntry.get())
        mycursor.execute(query, values)
        con.commit()

    messagebox.showinfo('Success', 'Successfull', parent=entryScreen)
    entryScreen.destroy()


def create_login_frame(window):
    ###frame for login screen
    LogFrame = Frame(window)
    LogFrame.place(x=300, y=100)

    ##Imahine declarations
    


    logoLabel = Label(LogFrame, image=userImage)
    logoLabel.grid(row=0, column=0, columnspan=2, pady=10)

    usernameLabel = Label(LogFrame, image=usernameImage, text='Username', compound=LEFT, font =('time new roman', 20, 'bold'))
    usernameLabel.grid(row=1, column=0, pady=10, padx=20)

    userEntry = Entry(LogFrame,bd=5, font=('Segoe UI', 20))
    userEntry.grid(row=1, column=1, pady=10, padx= 20)

    passLabel = Label(LogFrame, image=lockImage, text='Password', compound=LEFT, font =('time new roman', 20, 'bold'))
    passLabel.grid(row=2, column=0, pady=10, padx= 20)

    passEntry = Entry(LogFrame,bd=5, font=('Segoe UI', 20), show='*')
    passEntry.grid(row=2, column=1, pady=10, padx= 20)

    
    loginButton = Button(LogFrame, text='Login', font=('time new roman', 15, 'bold'),width= 15, fg= 'white',bg = 'blue', activebackground='cornflowerblue', activeforeground='white', cursor='hand2', command=lambda: log_in(userEntry,passEntry, window))
    loginButton.grid(row=3, column=1, pady=10)

    signUpButton = Button(LogFrame, text='Create account', font=('time new roman', 15, 'bold'),width= 15, fg= 'white',bg = 'forest green', activeforeground='forest green', cursor='hand2', command= lambda:sign_up(window))
    signUpButton.grid(row=4, column=1, pady=10)
    from auth.login import log_in, sign_up

