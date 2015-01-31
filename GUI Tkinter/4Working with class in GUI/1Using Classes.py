__author__ = 'AKHIL REDDY'

class AkkiClass:

    def __init__(self,master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame,text = "Print Button",command = self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame,text = "Quit",command = frame.quit)
        self.quitButton.pack(side = LEFT)

    def printMessage(self):
        print("I Think It's Working!!!")


from tkinter import *

root = Tk()
b = AkkiClass(root)
root.mainloop()
