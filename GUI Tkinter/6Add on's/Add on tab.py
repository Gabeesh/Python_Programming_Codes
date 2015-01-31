from tkinter import *

def doNothing():
    print('okay i wont')


root = Tk()

imageIcon = PhotoImage(file='camera.png')

menu = Menu(root)
root.config(menu=menu)#lav noget, lav en menu som er menu

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)#cascade betyder dropdown menu

subMenu.add_command(label="Add Item", command=doNothing)#tilf jer punkt til menuen
subMenu.add_separator()
subMenu.add_command(label="Preferences", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Copy", command=doNothing)

toolbar = Frame(root, bg='blue')
toolbutton1 = Button(toolbar, image=imageIcon, command=doNothing)
toolbutton1.pack(side=LEFT, padx=2, pady=2)#pad x/y er st rrelsen p  knappen
toolbutton2 = Button(toolbar, text='Print', command=doNothing)
toolbutton2.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X,)


status = Label(root, text="Welcome", bd=1, relief=SUNKEN, anchor=W)#relief er design til dit label
status.pack(side=BOTTOM, fill=X)


root.mainloop()