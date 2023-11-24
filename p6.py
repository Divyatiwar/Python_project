from tkinter import*
root=Tk()
root.title('project')
root.geometry('1200x1200')

#img=photoImage(files="starbus.png")
#Label(root,Image=img).pack()

Label(root,text="Online Bus Booking System",font='arial 20',bg='sky blue',fg='red').grid(row=3,column=8,padx=55,pady=50)

Label(root,text='Add Bus Operator Details',font='arial 15',bg='white',fg='green').grid(row=5,column=8,padx=55,pady=50)

    
Label(root,text='Operator id').grid(row=7,column=0)
var=Entry(root)
var.grid(row=7,column=1)

Label(root,text='Name').grid(row=7,column=3)
var1=Entry(root)
var1.grid(row=7,column=4)

Label(root,text='Address').grid(row=7,column=6)
var2=Entry(root)
var2.grid(row=7,column=7)

Label(root,text='Phone').grid(row=7,column=9)
var3=Entry(root)
var3.grid(row=7,column=10)

Label(root,text='Email').grid(row=7,column=12)
var4=Entry(root)
var4.grid(row=7,column=13)

def fun():
    Label(root,text=var.get()+var1.get()+var2.get()+var3.get()+var4.get()).grid(row=9,column=8,padx=55,pady=50)
Button(root,text='Add',bg='light green',fg='black',command=fun).grid(row=7,column=14,padx=25,pady=50)

Button(root,text='Edit',bg='light green',fg='black').grid(row=7,column=16,padx=25,pady=50)

root.mainloop()
