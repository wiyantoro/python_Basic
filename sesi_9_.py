import mysql.connector
from tkinter import *
from tkinter import messagebox
from subprocess import call

def  login():
    mysqldb=mysql.connector.Connect(host="Localhost", user="root",password="",database="latihan")
    mycursor=mysqldb.cursor()
    
    username=entry1.get()
    password=entry2.get()
    
    
    sql="select * from login where username= %s and password=%s"
    mycursor.execute(sql,[(username),(password)])
    result=mycursor.fetchall()
    
    
    if result:
        messagebox.showinfo("","Login Successs")
        root.destroy()
        
        
        return True
    
    else:
        messagebox.showinfo("", "Incorrect username and password")
        return False
    
root=Tk()
root.title("login")
root.geometry("300x200")

global entry1
global entry2

Label(root,text="username").place(x=20,y=20)
Label(root,text="password").place(x=20,y=70)

entry1=Entry(root,bd=5)
entry1.place(x=140,y=20)

entry2=Entry(root,bd=5)
entry2.place(x=140,y=70)

Button(root,text="login",command=login,height=3,width=13,bd=6).place(x=100,y=120)
root.mainloop()