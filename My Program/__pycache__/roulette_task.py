from tkinter import*

win = Tk()

win.geometry("500x250")

label1 = Label(win, text='Position1', font=("Calibri, 12"))

label1.grid(column=1, row=2)

label2 = Label(win, text='Position2', font=("Calibri, 12"))

label2.grid(column=3, row=5)

label3 = Label(win, text='Position3', font=("Calibri, 12"))

label3.grid(column=5, row=8)

label4 = Label(win, text='Position4', font=("Calibri, 12"))

label4.grid(column=7, row=11)

win.rowconfigure(9)

win.columnconfigure(9)

win.mainloop()




