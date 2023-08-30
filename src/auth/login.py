from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from auth.helper import verify_login, new_user
from PIL import ImageTk, Image

##log in verification
def log_in(userEntry,passEntry,window):
    if userEntry.get() == '' or passEntry.get() == '':
        messagebox.showerror('Error', 'Fields cannot be empty')
    elif verify_login(userEntry.get(), passEntry.get()):
        global username
        username = userEntry.get()
        messagebox.showinfo('Success',' Welcome' )
        window.destroy()
        from core import interface
    else:
        messagebox.showerror('Error', 'Please enter correct credentials')
###New user    
def sign_up(window):
    entryScreen= Toplevel()
    entryScreen.title('Registration form')
    entryScreen.grab_set()
    entryScreen.resizable(False, False)

    ico = Image.open('../image/Z.png')
    icon = ImageTk.PhotoImage(ico)
    entryScreen.wm_iconphoto(False, icon)

    emailLabel= Label(entryScreen, text='Email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    emailEntry = Entry(entryScreen, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=0, column=1, pady=15, padx=10)

    userLabel = Label(entryScreen, text='Username', font=('times new roman', 20, 'bold'))
    userLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    userEntry = Entry(entryScreen, font=('roman', 15, 'bold'), width=24)
    userEntry.grid(row=1, column=1, pady=15, padx=10)

    passLabel = Label(entryScreen, text='Password', font=('times new roman', 20, 'bold'))
    passLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    passEntry = Entry(entryScreen, font=('roman', 15, 'bold'), width=24, show='*')
    passEntry.grid(row=2, column=1, pady=15, padx=10)

    student_button = ttk.Button(entryScreen, text='Sign up', command=lambda: new_user(userEntry, passEntry, emailEntry,entryScreen, window))
    student_button.grid(row=7, columnspan=2, pady=15)
