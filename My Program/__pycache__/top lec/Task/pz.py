from tkinter import *
import tkinter
import random
screen = tkinter.Tk()
screen.title("ROULETTE")
screen.config(background="green")
screen.geometry("900x750")

displayVariable = StringVar()
uservariable = StringVar()
user=random.choice
def randnum(event):
	
	value =random.randint(1,12)
	
	updateDisplay(value)
    


def updateDisplay(myString):
	displayVariable.set(myString)

def randnum_1(event):
	
	value =random.randint(13,24)
	
	updateDisplay_1(value)

def updateDisplay_1(myString):
	displayVariable.set(myString)


# button_1 = Button(root, text="test")
# button_1.bind("<Button-1>",randnum)
# button_1.pack()
# displayVariable = StringVar()
# displayLabel = Label(screen, textvariable=displayVariable)
# displayLabel.pack()
# root.mainloop()


# from roulette_logic import *

btn = tkinter.Button(screen,text="0",font=("arial",18,"bold"),bg="green",fg="white",height=1,width=3)
btn.grid(row=0,column=0,rowspan=3)


btn1= tkinter.Button(screen,text="2to1",font=("arial",18,"bold"),bg="green",fg="white",height=1,width=3)
btn1.grid(row=0,column=14)
btn1.bind("<Button-1>",randnum)



btn2 = tkinter.Button(screen,text="2to1",font=("arial",18,"bold"),bg="green",fg="white",height=1,width=3)
btn2.grid(row=1,column=14)

btn3 = tkinter.Button(screen,text="2to1",font=("arial",18,"bold"),bg="green",fg="white",height=1,width=3)
btn3.grid(row=2,column=14)

count=0

for j in range(3,37,3):
    #button=tkinter.Button(screen,text=j,font=("ariel",18,"bold"))
    if j==6 or j==15 or j==24 or j==33:
         button=tkinter.Button(screen,text=j,font=("ariel",18,"bold"),bg="black",fg="white",padx=2,pady=2,height=1,width=3)
    else:
          button=tkinter.Button(screen,text=j,font=("ariel",18,"bold"),bg="red",fg="white",padx=2,pady=2,height=1,width=3)
    button.grid(row=0,column=count+1)
    count+=1
  
count2=0
for j in range(2,36,3):
    button=tkinter.Button(screen,text=j,font=("ariel",18,"bold"),bg="red",padx=2,pady=2,height=1,width=3)
    if j==5 or j==14 or j==23 or j==32:
         button=tkinter.Button(screen,text=j,font=("ariel",18,"bold"),bg="red",fg="white",padx=2,pady=2,height=1,width=3)
    else:
          button=tkinter.Button(screen,text=j,font=("ariel",18,"bold"),bg="black",fg="white",padx=2,pady=2,height=1,width=3)
    button.grid(row=1,column=count2+1)
    count2+=1

count3=0
for j in range(1,35,3):
    button=tkinter.Button(screen,text=j,font=("ariel",18,"bold"))
    if j==1 or j==7 or j==16 or j==19 or j==25 or j==34:
         button=tkinter.Button(screen,text=j,font=("ariel",18,"bold"),bg="red",fg="white",padx=2,pady=2,height=1,width=3)
    else:
          button=tkinter.Button(screen,text=j,font=("ariel",18,"bold"),bg="black",fg="white",padx=2,pady=2,height=1,width=3)
    button.grid(row=2,column=count3+1)
    count3+=1
# count4=0    
# for j in range(3):
#  button=tkinter.Button(screen,text=j,font=("ariel",18,"bold"),height=1,width=7)
#  button.grid(row=3,column=count4+1)
#  count4+=1
 

button1=tkinter.Button(screen,text="1 to 12",font=("ariel",18,"bold"),bg="green",fg="white",height=1,width=15,padx=2,pady=2)
button1.bind("<Button-1>",randnum)
button1.place(x=54,y=160)


button2=tkinter.Button(screen,text="13 to 24",font=("ariel",18,"bold"),bg="green",fg="white",height=1,width=15,padx=2,pady=2)
button2.bind("<Button-1>",randnum_1)
button2.place(x=280,y=160)

button3=tkinter.Button(screen,text="25 to 36",font=("ariel",18,"bold"),bg="green",fg="white",height=1,width=15,padx=2,pady=2)
button3.place(x=500,y=160)

# button4=tkinter.Button(screen,text="1 to 18",font=("ariel",18,"bold"),bg="green",fg="white",height=1,width=7,padx=2,pady=2)
# button4.place(x=54,y=213)

button5=tkinter.Button(screen,text="1 to 18",font=("ariel",18,"bold"),bg="green",fg="white",height=1,width=7,padx=2,pady=2)
button5.place(x=54,y=213)

button6=tkinter.Button(screen,text="EVEN",font=("ariel",18,"bold"),bg="green",fg="white",height=1,width=7,padx=2,pady=2)
button6.place(x=164,y=213)

# button7=tkinter.Button(screen,Text="ddsfsdf",font=("ariel",18,"bold"),bg="red",height=1,width=7,padx=2,pady=2)
# button7.place(x=280,y=213)

butto11=tkinter.Button(screen,font=("ariel",18,"bold"),bg="Red",height=1,width=7,padx=2,pady=2)
butto11.place(x=280,y=213)

button8=tkinter.Button(screen,text="Black",font=("ariel",18,"bold"),bg="Black",height=1,width=7,padx=2,pady=2)
button8.place(x=387,y=213)

button9=tkinter.Button(screen,text="ODD",font=("ariel",18,"bold"),bg="green",fg="white",height=1,width=8,padx=2,pady=2)
button9.place(x=500,y=213)

button10=tkinter.Button(screen,text="19 t0 36",font=("ariel",18,"bold"),bg="green",fg="white",height=1,width=7,padx=2,pady=2)
button10.place(x=619,y=213)

lbl1 = tkinter.Label(screen,textvariable="",font=("arial",12,"bold"),bg="black",fg="white",height=5,width=12)
lbl1.place(x=600,y=380)

lbl_user_score = tkinter.Label(screen,textvariable=displayVariable,font=("arial",12,"bold"),bg="white",fg="black",height=5,width=12)
lbl_user_score.place(x=650,y=480)
# lbl_user_score.pack()

screen.mainloop()