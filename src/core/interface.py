#interface.py
# Import required modules
from tkinter import *
import tkinter as tk
import time
from tkinter import ttk, filedialog, Toplevel
from tkcalendar import Calendar, DateEntry
from core.logic import (db_connect, execute_db_query, add_Purchase,
                        search_Data, remove_Purchase, update_table_from_database,
                        load_Data, export_Data, display_Data, Exit)

global dateEntry,descrEntry,amountEntry,classEntry,entryScreen,root, table
def entryAll(title, button, command):
    entryScreen= Toplevel()
    entryScreen.title(title)
    entryScreen.grab_set()
    entryScreen.resizable(False, False)

    dateLabel= Label(entryScreen, text='Date', font=('times new roman', 20, 'bold'))
    dateLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    dateEntry = DateEntry(entryScreen, font=('roman', 15, 'bold'), width=24,date_pattern='y/m/d')
    dateEntry.grid(row=0, column=1, pady=15, padx=10)

    descrLabel = Label(entryScreen, text='Description', font=('times new roman', 20, 'bold'))
    descrLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    descrEntry = Entry(entryScreen, font=('roman', 15, 'bold'), width=24)
    descrEntry.grid(row=1, column=1, pady=15, padx=10)

    amountLabel = Label(entryScreen, text='Amount', font=('times new roman', 20, 'bold'))
    amountLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    amountEntry = Entry(entryScreen, font=('roman', 15, 'bold'), width=24)
    amountEntry.grid(row=2, column=1, pady=15, padx=10)

    classLabel = Label(entryScreen, text='classification', font=('times new roman', 20, 'bold'))
    classLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    classEntry = Entry(entryScreen, font=('roman', 15, 'bold'), width=24)
    classEntry.grid(row=3, column=1, pady=15, padx=10)

    student_button = ttk.Button(entryScreen, text=button, command=command)
    student_button.grid(row=7, columnspan=2, pady=15)
    pass


def clock():
    date = time.strftime('%d/%m/%Y')
    Time = time.strftime('%H:%M:%S')
    datetimelabel.configure(text=f'    Date: {date}\nTime: {Time}')
    datetimelabel.after(1000, clock)

##lettering  
counter = 0
text= ''
def lettering():
    global text, counter 
    if counter == len(s):
        counter =0
        text = ''
    text = text+s[counter]
    letteringLabel.configure(text=text)
    counter+= 1
    letteringLabel.after(300, lettering)


root = Tk()

style = ttk.Style(root)  #ttkk style
root.tk.call("source", "../theme/forest-light.tcl")
root.tk.call("source", "../theme/forest-dark.tcl")
style.theme_use("forest-dark")


root.geometry('1200x680+0+0')
root.resizable(0,0)
root.title('Finance Tracker')

datetimelabel = Label(root, font=('times new roman', 18, 'bold'))
datetimelabel.place(x=5, y=5)

frame = Frame(root)
frame.pack()

clock()  # Start the clock function to update the time

##Display the application name with a slider
s='Finance Tracker'
letteringLabel= Label(root,font=('arial', 28, 'italic bold'), width= 30)
letteringLabel.place(x=200, y= 0)
lettering()

def enable_buttons():
    addPurchase['state'] = NORMAL
    searchData['state'] = NORMAL
    removePurchase['state'] = NORMAL
    displayData['state'] = NORMAL
    loadData['state'] = NORMAL
    exportData['state'] = NORMAL
    Connect['state'] = DISABLED

def new_db_connect():
    conn = db_connect(root,table)
    if conn:
        enable_buttons()

Connect = Button(root, text="Connect Database", command=new_db_connect)
Connect.place(x=900,y=0)




options= Frame(root)
options.place(x=50,y=80, width=300, height=600)

logo3= PhotoImage(file='../image/Flogo.png')
logo3_label= Label(options, image=logo3)
logo3_label.grid(row=0, column = 0)

addPurchase = Button(options, text='Add transaction', width=25, state=DISABLED, command=lambda :entryAll('Add Purchase','Add', lambda: add_Purchase(dateEntry.get(), descrEntry.get(), amountEntry.get(), classEntry.get(), entryScreen, root)))
addPurchase.grid(row=1, column =0, pady=20)

searchData= Button(options, text='Search transactions', width=25, state=DISABLED, command=lambda : entryAll('Search Data', 'Search',lambda: search_Data(dateEntry.get(), descrEntry.get(), amountEntry.get(), classEntry.get(), entryScreen,table)))
searchData.grid(row=2, column =0, pady=20)

removePurchase = Button(options, text='Remove transaction', width=25, state=DISABLED, command= lambda: remove_Purchase(table, root))
removePurchase.grid(row=3, column =0, pady=20)

displayData= Button(options, text='Display Spending', width=25, state=DISABLED, command=lambda: display_Data(root))
displayData.grid(row=4, column =0, pady=20)

loadData = Button(options, text='Load from external', width=25, state=DISABLED, command= lambda: load_Data(root))
loadData.grid(row=5, column =0, pady=20)

exportData = Button(options, text='Export data', width=25, state=DISABLED,command=lambda: export_Data(table,root))
exportData.grid(row=6, column =0, pady=20)

exitButton = Button(options, text='Exit', width=25, command=lambda: Exit(root))
exitButton.grid(row=7, column =0, pady=20)

rightFrame= Frame(root)
rightFrame.place(x=350,y=80, width=820, height=600)

scrollBarX= Scrollbar(rightFrame, orient=HORIZONTAL)
scrollBarY= Scrollbar(rightFrame, orient=VERTICAL)


table=ttk.Treeview(rightFrame, columns=('Date', 'Description',
                                         'Amount','Balance', 'Classification'),
                                         xscrollcommand=scrollBarX.set, yscrollcommand=scrollBarY.set)
scrollBarX.config(command=table.xview)
scrollBarY.config(command=table.yview)

scrollBarX.pack(side=BOTTOM, fill= X)
scrollBarY.pack(side=RIGHT, fill= Y)

table.pack(fill=BOTH, expand=1)

table.heading('Date', text='Date')
table.heading('Description', text='Description')
table.heading('Amount', text='Amount')
table.heading('Balance', text='Balance')
table.heading('Classification', text='Classification')

table.config(show='headings')


root.mainloop()





