from tkinter import*
#from PIL import ImageTk, Image
root=Tk()
root.title('page 1')
root.geometry('1200x1200')

#img = ImageTk.PhotoImage(Image.open("starbus.png"))
#panel = Label(root, image = img,height=5,width=15)
#panel.pack( fill = "both", expand = "yes")

Label(root,text='Online Bus Booking system',font="arial 30",bg="sky blue",fg="red").pack()

Label(root,text='Name : DIVYA TIWARI',font="arial 20",fg="blue").pack(padx=35,pady=30)

Label(root,text='Enrollment number: 221B149',font="arial 20",fg="blue").pack(padx=35,pady=30)

Label(root,text='Mobile : 6266193282 ',font="arial 20",fg="blue").pack(padx=35,pady=30)

Label(root,text='Submitted to : Mahesh kumar ',font="arial 30",bg="sky blue",fg="red").pack(padx=35,pady=30)
Label(root,text='Project Based Learning',font='times 20 bold ',fg='red').pack()



root.mainloop()
