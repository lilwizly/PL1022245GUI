import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
def main():
    con = sqlite3.connect("Login.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS login_info(User_ID INTEGER  PRIMARY KEY, username varchar(255), password varchar(255))")
    con.commit()
    con.close()
def Login(username, password):
    con = sqlite3.connect("Login.db")
    cur = con.cursor()
    try:
        cur.execute("SELECT * FROM login_info WHERE username = ? AND password = ?", (username,password))
    except:
        main()
        cur.execute("SELECT * FROM login_info WHERE username = ? AND password = ?", (username, password))
    if_found=cur.fetchone()
    con.close()
    return(if_found)
    #con.close()


def CreateLOGINFO(x,y):
    main()

    con = sqlite3.connect("Login.db")
    cur = con.cursor()
    cur.execute(f"INSERT INTO login_info VALUES(null,?,?)",(x,y))
    tk.messagebox.showinfo(title="Sucess!",message= f'Username, Password inputted:{x},{y}')
    con.commit()
    con.close()
#to be tested
'''
def new_uswin():
    new_us = tk.Tk()
    us_pas1 = tk.StringVar()
    ps_pas1 = tk.StringVar()
    login_username_label = tk.Label(new_us, text="Username:")
    login_username_label.grid(row=0, column=0)
    login_username_entry = tk.Entry(new_us, width=20, textvariable=us_pas1)
    login_username_entry.grid(row=0, column=1)
    login_password_label = tk.Label(new_us, text="Password:")
    login_password_label.grid(row=1, column=0)
    login_password_entry = tk.Entry(new_us, width=20, textvariable=ps_pas1)
    login_password_entry.grid(row=1, column=1)
    login_button = ttk.Button(new_us, text="login", command=lambda: CreateLOGINFO(us_pas1.get(), ps_pas1.get()))
    login_button.grid(row=2, column=1)
    new_us.mainloop()
def logwindow():
    choice_window=tk.Tk()
    choice_window.title("Choice")
    choice_window.geometry("200x100")
    new_us_ps=ttk.Button(choice_window,text="Make New Username and Password", command=lambda :new_uswin())
    new_us_ps.grid(row=1,column=0)
    try_agin=ttk.Button(choice_window,text="Try Again", command=choice_window.destroy)
    try_agin.grid(row=0,column=0)
    choice_window.mainloop()
    
'''
def LogIN():
    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("400x500")
    us_pas=tk.StringVar()
    ps_pas=tk.StringVar()
    login_username_label = tk.Label(login_window, text="Username:")
    login_username_label.grid(row=0, column=0)
    login_username_entry = tk.Entry(login_window, width=20,textvariable=us_pas)
    login_username_entry.grid(row=0, column=1)
    login_password_label = tk.Label(login_window, text="Password:")
    login_password_label.grid(row=1, column=0)
    login_password_entry = tk.Entry(login_window, width=20,textvariable=ps_pas)
    login_password_entry.grid(row=1, column=1)
    login_button = ttk.Button(login_window, text="login", command=login_window.destroy)
    login_button.grid(row=2, column=1)
    login_button = ttk.Button(login_window, text="register new username-password pair", command=lambda :CreateLOGINFO(us_pas.get(), ps_pas.get()))
    login_button.grid(row=3, column=1)
    login_window.mainloop()
    if Login(us_pas.get(),ps_pas.get())==None:
       tk.messagebox.showinfo("Login Failed","Login Failed")
       #logwindow()
       LogIN()
    else:
        return {True:us_pas.get()}
#LogIN()