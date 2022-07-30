from tkinter import *
screen = Tk()
screen.title("MY APP")
screen.config(background="light blue")
screen.geometry("540x550")

firstname_text = Label(text="FirstName :")
lastname_text = Label(text="LastName :")
Email_text = Label(text="Email :")
con_num=Label(text="Contact Number:")
Vac=Label(text="Vaccination:")
 
firstname_text.place(x=15,y=70)
lastname_text.place(x=15,y=140)
Email_text.place(x=15,y=210)
con_num.place(x=15,y=280)
Vac.place(x=15,y=350)

firstname=StringVar()
lastname =StringVar()
Email = StringVar()
con_num=IntVar()
Vac=StringVar()
 
first_name_entry =Entry(textvariable=firstname,width="30")
last_name_entry = Entry(textvariable=lastname,width="30")
Email_entry = Entry(textvariable=Email,width="30")
con_num=Entry(textvariable=con_num,width=30)
Vac=Entry(textvariable=Vac,width=30)
 
first_name_entry.place(x=130,y=70)
last_name_entry.place(x=130,y=140)
Email_entry.place(x=130,y=210)
con_num.place(x=130,y=280)
Vac.place(x=130,y=350)

 
# button = Button(text="Submit Data",command=save_info,width="30",height="2",bg="grey")

button = Button(text="Submit Data",width="30",height="2",bg="grey")
 
button.place(x=100,y=450)
screen.mainloop()