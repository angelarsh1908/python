from logging import root
import tkinter
import random

screen = tkinter.Tk()
screen.title("MY APP")
screen.config(background="white")
screen.geometry("540x450")

def printinput():
    input=text1.get() 

lbl1 = tkinter.Label(screen,text="Firstname",font=("arial",12,"bold"),bg="white",fg="black")
lbl1.place(x=0,y=10)
text1=tkinter.Text(height=2,width=20,bd=5)
text1.pack()


var_result = tkinter.StringVar()
var_result.set("RESULT")
lbl2 = tkinter.Label(screen,text="Lastname",font=("arial",12,"bold"),bg="white",fg="black")
lbl2.place(x=1,y=50)
text2=tkinter.Text(height=2,width=20,bd=5)
text2.pack()

lbl3 = tkinter.Label(screen,text="Email",font=("arial",12,"bold"),bg="white",fg="black")
lbl3.place(x=1,y=100)
text3=tkinter.Text(height=2,width=20,bd=5)
text3.pack()

lbl4 = tkinter.Label(screen,text="Contact Number",font=("arial",12,"bold"),bg="white",fg="black")
lbl4.place(x=1,y=150)
text4=tkinter.Text(height=2,width=20,bd=5)
text4.pack()

lbl5 = tkinter.Label(screen,text="Vaccination Zone",font=("arial",12,"bold"),bg="white",fg="black")
lbl5.place(x=1,y=200)
text5=tkinter.Text(height=2,width=20,bd=5)
text5.pack()

btn_result = tkinter.Button(screen,textvariable=var_result,font=("arial",26,"bold"),bg="white",fg="black",bd=5,width=20)
btn_result.place(x=50,y=280)
screen.mainloop()