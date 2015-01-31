__author__ = 'AKHIL REDDY'
from tkinter import *

root = Tk()

# bd is border, relief is type of border
status = Label(root, text="Preparing to do nothing", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)


root.mainloop()



