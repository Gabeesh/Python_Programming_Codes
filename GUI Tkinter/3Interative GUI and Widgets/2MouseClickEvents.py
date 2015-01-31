__author__ = 'AKHIL REDDY'
from tkinter import *

root = Tk()

def LeftClick(event):
    print("LeftClick")

def MiddleClick(event):
    print("MiddleClick")

def RightClick(event):
    print("RightClick")

frame = Frame(root,width = 500,height = 300)
frame.bind("<Button-1>", LeftClick )
frame.bind("<Button-2>", MiddleClick )
frame.bind("<Button-3>",RightClick )
frame.pack()

root.mainloop()

