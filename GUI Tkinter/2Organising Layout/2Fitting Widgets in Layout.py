__author__ = 'AKHIL REDDY'

from  tkinter import *

root = Tk()

one = Label(root,text = "One",bg = "blue", fg = "yellow")
one.pack()
two = Label(root,text = "Two",bg = "red", fg = "black")
two.pack(fill = X)
three = Label(root,text = "Three",bg = "green", fg = "white")
three.pack(side = RIGHT , fill = Y)


root.mainloop()

