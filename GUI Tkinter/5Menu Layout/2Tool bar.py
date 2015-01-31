from tkinter import *

def doNothing():
    print("ok ok I won't...")

root = Tk()

toolbar = Frame(root, bg="snow")

insertButt = Button(toolbar, text="Insert Image", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt = Button(toolbar, text="Print", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)


root.mainloop()



