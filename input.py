from tkinter import *

root = Tk()

e = Entry(root, width=40)
e.pack()
e.insert(0, "Enter your name: ")

def myClick():
    myLabel = Label(root, text="Hello " + e.get())
    myLabel.pack()

myButton = Button(root, text="Enter your name", command=myClick, fg="white", bg="blue")
myButton.pack()

root.mainloop()