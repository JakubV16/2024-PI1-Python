import tkinter
import random


Canvas=tkinter.Canvas()
Canvas.pack()

pokus = 1

def akcia():
    global pokus
    cisloMOJE = int(textbox.get())
    if cisloMOJE < cisloPC:
        label.config(text="Dal si menšie číslo")
        pokus += 1
    elif cisloMOJE > cisloPC:
        label.config(text="Dal si väčšie číslo")
        pokus += 1
    else:
        label.config(text=f"Uhádol si, počet pokusov bolo {pokus}")

cisloPC=random.randint(0, 9)







label=tkinter.Label()
label.pack()

textbox=tkinter.Entry()
textbox.pack()

buttom=tkinter.Button(text="Hádaj", command= akcia)
buttom.pack()







tkinter.mainloop()