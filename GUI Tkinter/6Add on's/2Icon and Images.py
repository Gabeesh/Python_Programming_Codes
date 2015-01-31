__author__ = 'AKHIL REDDY'
from tkinter import *

root = Tk()
photo = PhotoImage(file="lilly.png")
label = Label(root, image=photo)
label.pack()
root.mainloop()
