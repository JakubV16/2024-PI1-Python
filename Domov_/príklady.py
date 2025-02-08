import tkinter
import random

canvas=tkinter.Canvas()
canvas.pack()

x=random.randint(0,10)
y=random.randint(0,10)
priklady=random.choice([f"{x}+{y}", f"{x}-{y}", f"{y}+{x}", f"{y}-{x}"])
vysledok=eval(priklady)
def akcia():
    for i in range(20):
        global priklady
        Cislomoje = int(Textbox.get())
        if Cislomoje == vysledok:
            label.config(text=f"Správne výsledok príkladu {priklady} je {vysledok}")
        else:
            label.config(text="Nesprávne!")
        

label=tkinter.Label(text=priklady)
label.pack()

Textbox=tkinter.Entry()
Textbox.pack()

buttom=tkinter.Button(text="Potvrdzujem", command= akcia)
buttom.pack()




































tkinter.mainloop()