from roulette_logic import *

btn = tkinter.Button(screen,text=0,font=("arial",18,"bold"),bg="white",fg="black")
btn.grid(row=0,column=0,rowspan=3)

count=0
for j in range(3,37,3):
    button=tkinter.Button(screen,text=j,font=("ariel",18,"bold"))
    button.grid(row=0,column=count+1)
    count+=1

count2=0
for j in range(2,36,3):
    button=tkinter.Button(screen,text=j,font=("ariel",18,"bold"))
    button.grid(row=1,column=count2+1)
    count2+=1

count3=0
for j in range(1,35,3):
    button=tkinter.Button(screen,text=j,font=("ariel",18,"bold"))
    button.grid(row=2,column=count3+1)
    count3+=1




screen.mainloop()