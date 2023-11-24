from tkinter import *
root=Tk()
root.title('page 7')
root.geometry('1200x1200')

Label(root,text="Online Bus Booking System",font='arial 15 bold',bg='sky blue',fg='red').grid(row=3,column=6,padx=55,pady=50)

Label(root,text='Add Bus Details',font='arial 15 bold',bg='white',fg='green').grid(row=5,column=6,padx=55,pady=50)
Label(root,text='Bus ID',font='arial 10 bold').grid(row=7,column=0)
var=Entry(root)
var.grid(row=7,column=1)

Label(root,text='Bus Type',font='arial 10 bold').grid(row=7,column=2)
var1=StringVar()
var1.set("Bus Type ")
option=["AC 2x2","AC 3x2","NON AC 2x2","NON AC 3x2","AC SLEEPER 2x1","NON AC-SLEEPER 2x1"]
OptionMenu(root,var1,*option).grid(row=7,column=3)

Label(root,text='Capacity',font='arial 10 bold').grid(row=7,column=4)
var2=Entry(root)
var2.grid(row=7,column=5)

Label(root,text='Fare Rs',font='arial 10 bold').grid(row=7,column=7)
var3=Entry(root)
var3.grid(row=7,column=8)

Label(root,text='Operator ID',font='arial 10 bold').grid(row=7,column=9)
var4=Entry(root)
var4.grid(row=7,column=10)

Label(root,text='Route ID',font='arial 10 bold').grid(row=7,column=11)
var5=Entry(root)
var5.grid(row=7,column=12)
Button(root,text='Add Bus',font='arial 10 bold',bg='light green',fg='black').grid(row=9,column=7,padx=25,pady=50)
Button(root,text='Edit Bus',font='arial 10 bold',bg='light green',fg='black').grid(row=9,column=8,padx=25,pady=50)
root.mainloop()
