from tkinter import*
root=Tk()
root.title('page 5')
root.geometry('1200x1200')

#img=photoImage(files="starbus.png")
#Label(root,Image=img).pack()

Label(root,text="Online Bus Booking System",font='arial 30',bg='sky blue',fg='red').grid(row=3,column=3,padx=55,pady=50)

Label(root,text='Add new details to database',font='arial 20',bg='white',fg='green').grid(row=5,column=3,padx=55,pady=50)

Button(root,text='New operator',font='arial 15',bg='light green',fg='black').grid(row=8,column=0,padx=25,pady=50)

Button(root,text='New Bus',font='arial 15',bg='orange',fg='black').grid(row=8,column=2,padx=25,pady=50)

Button(root,text='New Route',font='arial 15',bg='sky blue',fg='black').grid(row=8,column=4,padx=25,pady=50)

Button(root,text='New Run',font='arial 15',bg='pink',fg='black').grid(row=8,column=6,padx=25,pady=50)

root.mainloop()
