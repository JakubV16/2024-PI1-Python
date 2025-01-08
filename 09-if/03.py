import tkinter

Canvas=tkinter.Canvas()
Canvas.pack()

def akcia():
    label.config(text = textbox.get())

label=tkinter.Label()
label.pack()

textbox=tkinter.Entry()
textbox.pack()

buttom=tkinter.Button(text="VYTLAXC", command= akcia)
buttom.pack()

tkinter.mainloop()