from tkinter import*
root=Tk()
root.title('page 2')
root.geometry('1200x1200')


Label(root,text='Online Bus Booking system',font="arial 40",bg="sky blue",fg="red").grid(row=3,column=6,padx=45,pady=50)

Button(root,text='Seat Booking',font='arial 20',bg='light green').grid(row=8,column=0,padx='50',pady='85')
Button(root,text='Checked booked seat',font='arial 20',bg='light green').grid(row=8,column=6,padx='50',pady='85')
Button(root,text='Add bus details',font='arial 20',bg='light green').grid(row=8,column=8,padx='50',pady='85')

Label(root,text='For Admin Only',font='Arial 15',fg='Red').grid(row=9,column=8)
root.mainloop()
