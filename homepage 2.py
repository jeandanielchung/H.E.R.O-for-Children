# Homepage

# Profile of each child

from tkinter import *

master = Tk()
Label(master, text="Search by Name").grid(row=0)
e1 = Entry(master)

e1.grid(row=0, column=1)

var1 = IntVar()
Checkbutton(master, text="Demographic", variable=var1).grid(row=1)

def callback():
    print("click")

b = Button(master, text="Search by Name", command=callback)
b.pack()
mainloop()

