__author__ = 'AKHIL REDDY'
from tkinter import *

root = Tk()

def printName():
    print("I am Akhil Reddy")
def printBro(event):
    print("My Bro Name is Lilly")

button_1 = Button(root, text = "Print Name",bg = 'green', command = printName)
button_1.pack()

button_2 = Button(root, text = "Print BroName",bg = 'red')
button_2.bind("<Button-1>",printBro)
button_2.pack()

root.mainloop()

