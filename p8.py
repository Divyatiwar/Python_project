from tkinter import *
root=Tk()
root.title('page 8')
root.geometry('1200x1200')

Label(root,text="Online Bus Booking System",font='arial 25',bg='sky blue',fg='red').grid(row=3,column=6,padx=55,pady=50)

Label(root,text='Add Bus Route Details',font='arial 20 bold',bg='white',fg='green').grid(row=5,column=6,padx=55,pady=50)
Label(root,text='Route ID',font='arial 10 bold').grid(row=7,column=0)
var=Entry(root)
var.grid(row=7,column=1)

Label(root,text='Station Name',font='arial 10 bold').grid(row=7,column=2)
var1=Entry(root)
var1.grid(row=7,column=3)

Label(root,text='Station ID',font='arial 10 bold').grid(row=7,column=4)
var2=Entry(root)
var2.grid(row=7,column=5)

Button(root,text='Add Route',font='arial 10 bold',bg='light green',fg='black').grid(row=7,column=7,padx=25,pady=50)
Button(root,text='Delete Route',font='arial 10 bold',bg='light green',fg='Red').grid(row=7,column=9,padx=25,pady=50)
root.mainloop()
