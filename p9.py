from tkinter import *
root=Tk()
root.title('page 9')
root.geometry('1200x1200')

Label(root,text="Online Bus Booking System",font='arial 25',bg='sky blue',fg='red').grid(row=3,column=6,padx=55,pady=50)

Label(root,text='Add Bus Running Details',font='arial 20 bold',bg='white',fg='green').grid(row=5,column=6,padx=55,pady=50)
Label(root,text='Bus ID',font='arial 10 bold').grid(row=7,column=0)
var=Entry(root)
var.grid(row=7,column=1)

Label(root,text='Running Detail',font='arial 10 bold').grid(row=7,column=2)
var1=Entry(root)
var1.grid(row=7,column=3)

Label(root,text='Seat Available',font='arial 10 bold').grid(row=7,column=4)
var2=Entry(root)
var2.grid(row=7,column=5)

def fun1():
    Label(root,text=var.get()+var1.get()+var2.get()).grid(row=9,column=2)
def fun2():
    Label(root,text=var.get()+var1.get()+var2.get()).grid(row=9,column=2)

Button(root,text='Add Run',command=fun1,font='arial 10 bold',bg='light green',fg='black').grid(row=7,column=7,padx=25,pady=50)
Button(root,text='Delete Run',command=fun2,font='arial 10 bold',bg='light green',fg='Red').grid(row=7,column=9,padx=25,pady=50)
root.mainloop()
