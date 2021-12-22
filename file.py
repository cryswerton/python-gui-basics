from tkinter import *
from tkinter import filedialog

root = Tk()

root.filename = filedialog.askopenfilename(initialdir="C:\\Users\\crysw\\Pictures", title="Select a File", filetypes=(("png files", "*.png"), ("all files", "*.*")))
my_label = Label(root, text=root.filename).pack()

root.mainloop()