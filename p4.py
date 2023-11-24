from tkinter import*
root=Tk()
root.title('page 4')
root.geometry('1200x1200')

#img=photoImage(files="starbus.png")
#Label(root,Image=img).pack()

Label(root,text="Online Bus Booking System",font='arial 40',bg='sky blue',fg='red').grid(row=3,column=2,padx=55,pady=50)

Label(root,text="Check Your Booking",font='arial 20 bold',bg='light green',fg='black').grid(row=5,column=2,padx=55,pady=50)

Label(root,text='Enter your Mobile no:',font='arial 15').grid(row=7,column=0,padx=25,pady=50)
var=Entry(root)
var.grid(row=7,column=1,padx=55,pady=50)

Button(root,text='check Booking',font='arial 10').grid(row=7,column=3,padx=25,pady=50)
root.mainloop()
