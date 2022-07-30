import tkinter
from tkinter import font
from turtle import Screen
Screen=tkinter.Tk()
Screen.title("My App")
Screen.geometry("500x500")
btn1=tkinter.Button(Screen,text="ok",bg="yellow",fg="blue",font=("arial",12,"italic"),activebackground="orange",activeforeground="black",height=2,width=8,bd=8)
#btn1.pack(side=tkinter.LEFT)

btn2=tkinter.Button(Screen,text="cancel",bg="yellow",fg="blue",font=("arial",12,"italic"),activebackground="orange",activeforeground="black",height=2,width=8,bd=8)
#btn1.pack(side=tkinter.LEFT)
#btn1.place(x=0,y=0)
#btn2.place(x=1,y=1)
btn1.grid(row=0,column=0)
btn2.grid(row=0,column=1)
Screen.mainloop()

