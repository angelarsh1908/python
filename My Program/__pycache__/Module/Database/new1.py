import tkinter
from new_db import *


firstname_text =tkinter.Label(text="FirstName :")
lastname_text =tkinter.Label(text="LastName :")
Email_text = tkinter.Label(text="Email :")
contact=tkinter.Label(text="Contact Number:")
Vac=tkinter.Label(text="Vaccination:")
 
firstname_text.place(x=15,y=70)
lastname_text.place(x=15,y=140)
Email_text.place(x=15,y=210)
contact.place(x=15,y=280)
Vac.place(x=15,y=350)
 
first_name_entry =tkinter.Entry(textvariable=firstname,width=30)
last_name_entry = Entry(textvariable=lastname,width="30")
Email_entry = Entry(textvariable=Email,width="30")
con_num_entry=Entry(textvariable=contact,width="30")
Vacc_entry=Entry(textvariable=Vac,width="30")
 
first_name_entry.place(x=130,y=70)
last_name_entry.place(x=130,y=140)
Email_entry.place(x=130,y=210)
con_num_entry.place(x=130,y=280)
Vacc_entry.place(x=130,y=350)

 
button =tkinter.Button(screen,text="Submit Data",width="30",height="2",bg="grey",command=insertData)
 
button.pack()

button.place(x=0,y=450)

button1 =tkinter.Button(screen,text="Search Data",width="30",height="2",bg="grey",command=op_window)

button1.pack()
button1.place(x=250,y=450)

button2=tkinter.Button(screen,text="delete Data",width="30",height="2",bg="grey",command=dltdata)

button2.pack()
button2.place(x=0,y=550)

button3=tkinter.Button(screen,text="delete Data",width="30",height="2",bg="grey",command=op_window)

button3.pack()
button3.place(x=250,y=550)

screen.mainloop()