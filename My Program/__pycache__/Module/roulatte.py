from cProfile import label
from re import X
from textwrap import fill
import tkinter
from tkinter import Tk,Frame,Label,Button
from tkinter.tix import COLUMN
mainwindow=Tk()
mainframe=Frame(mainwindow,bg="green")
mainframe.pack(fill="both",expand=True)

# screen = tkinter.Tk()
# screen.title("Roulette")
# screen.config(background="green")
# screen.geometry("1200x500")
n=10
i=3
grid_frame=Frame(mainframe)
for row in range(7):
    for column in range(14):
        label=Label(grid_frame,text="item",bg="red",fg="black",padx=5,pady=5)
        label.grid(row=row,column=column,padx="2",pady="2")
        for j in range(n):
           mybutton= Button(text=j)
           mybutton.grid(row=i,column=j)
grid_frame.pack()

mainwindow.mainloop()

# # number of buttons
# n=10

# #Defining the row and column
# i=3

# #Iterating over the numbers till n and
# #creating the button
# for j in range(n):
#    mybutton= Button(win, text=j)
#    mybutton.grid(row=i, column=j)

# # Keep the window open
# win.mainloop()
