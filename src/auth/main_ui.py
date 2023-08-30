from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from auth.helper import set_style, create_login_frame, load_env_vars
from auth.login import log_in, sign_up


def main():
    window = Tk()
    window.title("Login")
    window.geometry('1200x600+0+0')
    window.resizable(False, False)
    
    
    load_env_vars()
    set_style(window)
    
    LogFrame = create_login_frame(window)
    
    window.mainloop()

if __name__ == "__main__":
    main()
