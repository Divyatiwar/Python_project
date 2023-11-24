from tkinter import*
root=Tk()
root.title('page 3')
root.geometry('1200x1200')

#img=photoImage(files="starbus.png")
#Label(root,Image=img).pack()

Label(root,text="Online Bus Booking System",font='arial 30',bg='sky blue',fg='red').grid(row=3,column=5,padx=55,pady=50)

Label(root,text="Enter Journey Details",font="arial 20",bg="lime green",fg="black").grid(row=6,column=5,padx=55,pady=50)

Label(root,text='To',font='arial 10').grid(row=8,column=0,padx=25,pady=50)
var=Entry(root)
var.grid(row=8,column=1,padx=25,pady=50)

Label(root,text='From',font='arial 10').grid(row=8,column=3,padx=25,pady=50)
var1=Entry(root)
var1.grid(row=8,column=4,padx=25,pady=50)

Label(root,text='Journey Date',font='arial 10').grid(row=8,column=6,padx=25,pady=50)
var2=Entry(root)
var2.grid(row=8,column=7,padx=25,pady=50)


Button(root,text='show bus',font='arial 14',bg='green',fg='black').grid(row=8,column=9,padx=25,pady=50)
root.mainloop()
