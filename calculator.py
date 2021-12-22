from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4)

def button_add():
    return
# define buttons
btn1 = Button(root, text="1", padx=40, pady=20, command=button_add)
btn2 = Button(root, text="2", padx=40, pady=20, command=button_add)
btn3 = Button(root, text="3", padx=40, pady=20, command=button_add)
btn4 = Button(root, text="4", padx=40, pady=20, command=button_add)
btn5 = Button(root, text="5", padx=40, pady=20, command=button_add)
btn6 = Button(root, text="6", padx=40, pady=20, command=button_add)
btn7 = Button(root, text="7", padx=40, pady=20, command=button_add)
btn8 = Button(root, text="8", padx=40, pady=20, command=button_add)
btn9 = Button(root, text="9", padx=40, pady=20, command=button_add)
btn0 = Button(root, text="0", padx=40, pady=20, command=button_add)

# put the buttons on the screen

btn1.grid(row=3, column=1)
btn2.grid(row=3, column=2)
btn3.grid(row=3, column=3)

btn4.grid(row=2, column=1)
btn5.grid(row=2, column=2)
btn6.grid(row=2, column=3)

btn7.grid(row=1, column=1)
btn8.grid(row=1, column=2)
btn9.grid(row=1, column=3)

btn0.grid(row=4, column=1)

root.mainloop()