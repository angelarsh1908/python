# from cProfile import tkinter.label
# import cgi
# from cgitb import text
# from doctest import master
# import email
# from logging import root
# from sqlite3 import Row
import email
from tkinter import messagebox
# from turtle import width
# from venv import create
import tkinter
import pymysql
from tkinter import *

screen = Tk()
screen.title("MY APP")
screen.config(background="light blue")
screen.geometry("650x550")

mycon = pymysql.connect(host="localhost",user="root",password="",database="mydb")
mycursor = mycon.cursor()
s_id=int()
firstname=StringVar()
lastname =StringVar()
Email = StringVar()
contact=StringVar()
Vac=StringVar()

def insertData():
    fname=firstname.get()
    lname=lastname.get()
    email=Email.get()
    Contact=contact.get()
    vac=Vac.get()


    query = "insert into student(fname,lname,email,Contact,vac) values ('%s','%s','%s','%s','%s')"
    args = (fname,lname,email,Contact,vac)

    mycursor.execute(query%args)
    mycon.commit()

def dltdata():
    sql_query = "DELETE FROM student where id='1'"
    mycursor.execute(sql_query)
    mycon.commit()
   


def op_window():

    # tkinter=Tk()
    root=Tk()
    #top=Toplevel()
    root.geometry("500x650")
    root.config(background="light blue")
   
    # lbl1=Label(root,text="Id")
    lbl1=tkinter.Label(root,text="Search student detail here",width="20")
    lbl1.grid(row=0,column=0,columnspan=2)
    
    l11=Label(root,text="ID")
    l11.place(x=20,y=150)
    e11=Entry(root,textvariable=s_id)
    l1=Label(root,text="Firstname")
    e1=Entry(root,textvariable=firstname)
    l2=Label(root,text="lastname")
    e2=Entry(root,textvariable=lastname)
    l3=Label(root,text="Email")
    e3=Entry(root,textvariable=email)
    l4=Label(root,text="Contact")
    e4=Entry(root,textvariable=contact)
    l5=Label(root,text="Vaccination")
    e5=Entry(root,textvariable=Vac)
    b1=Button(root,text="Search",command=search)
    b2=Button(root,text="clear",command=clear)
    
    l11.grid(row=1,column=0)
    e11.grid(row=1,column=1)
    l1.grid(row=2,column=0)
    e1.grid(row=2,column=1)
    l2.grid(row=3,column=0)
    e2.grid(row=3,column=1)
    l3.grid(row=4,column=0)
    e3.grid(row=4,column=1)
    l4.grid(row=5,column=0)
    e4.grid(row=5,column=1)
    l5.grid(row=6,column=0)
    e5.grid(row=6,column=1)

                 
def search():
    try:
        mycon = pymysql.connect(host="localhost",user="root",password="",database="mydb")
        mycursor = mycon.cursor()
        sql="select * from dtudent where id='%s"%s_id.get()
        mycursor.execute(sql)
        result=mycursor.fetchone()
        fname=firstname.set(result[1])
        lname=lastname.set(result[2])
        email=email.set(result[3])
        Contact=contact.set(result[4])
        vac=Vac.set(result[5])
        mycon.close()
    except:
        messagebox.showinfo('No Data','No such data available....')
        clear()

def clear():
        fname=firstname.set('')
        lname=lastname.set('')
        email=email.set('')
        Contact=contact.set('')
        vac=vac.set('')

    
   
