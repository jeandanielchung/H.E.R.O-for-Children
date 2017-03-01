from tkinter import *

# Search by Name

def doNothing():
    print("Nothing yet..") 

root = Tk()

b = Button(root, text="Logout").grid(row=0, sticky=W) 
# b.pack()

w = Label(root, text="Welcome to your homepage.").grid(row=5, column=2)
# w.pack()

e = Entry(root).grid(row=8, column=2)
# e.pack()

var = StringVar(root)
var.set("Search Options")
option = OptionMenu(root, var, "Patient Names", "Medical Information").grid(row=9, column=2)
# option.pack()

b2 = Button(root, text="Add Patient").grid(row=10, column=2)  
# b2.pack() 

root.mainloop()


