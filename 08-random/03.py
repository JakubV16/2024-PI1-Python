import tkinter
import random

pocet = int(input("Zadaj počet jednotiek: "))

canvas = tkinter.Canvas(width =500, height = 400)
canvas.pack()

def jeden(x, y):
    canvas.create_rectangle(x, y+10, x+10, y+20,fill = random.choice(["red","green","blue","yellow","purple"]))
    canvas.create_rectangle(x+10, y, x+20, y+10,fill = random.choice(["red","green","blue","yellow","purple"]))
    canvas.create_rectangle(x+10, y+10, x+20, y+20,fill = random.choice(["red","green","blue","yellow","purple"]))
    canvas.create_rectangle(x+10, y, x+20, y+20,fill = random.choice(["red","green","blue","yellow","purple"]))
    canvas.create_rectangle(x+10, y+20, x+20, y+30,fill = random.choice(["red","green","blue","yellow","purple"]))
    canvas.create_rectangle(x+10, y+30, x+20, y+40,fill = random.choice(["red","green","blue","yellow","purple"]))
    canvas.create_rectangle(x+10, y+40, x+20, y+50,fill = random.choice(["red","green","blue","yellow","purple"]))
    canvas.create_rectangle(x+10, y+50, x+20, y+60,fill = random.choice(["red","green","blue","yellow","purple"]))
    canvas.create_rectangle(x+10, y+60, x+20, y+70,fill = random.choice(["red","green","blue","yellow","purple"]))
    canvas.create_rectangle(x, y+60, x+10, y+70,fill = random.choice(["red","green","blue","yellow","purple"]))
    canvas.create_rectangle(x+20, y+60, x+30, y+70,fill = random.choice(["red","green","blue","yellow","purple"]))



for i in range(pocet):
    jeden(random.randint(3,367),random.randint(3,327))
tkinter.mainloop()