from tkinter import *

root = Tk()

clicked = StringVar()
clicked.set("Option 1")
drop = OptionMenu(root, clicked, "Option 1", "Option 2", "Option 3")
drop.pack()

root.mainloop()