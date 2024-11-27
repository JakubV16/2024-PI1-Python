import tkinter 
import random

pocet = int(input("Zadaj počet štvorcov: "))
canvas_width = int(input("Zadaj šírku plátna: "))
canvas_height = int(input("Zadaj výšku plátna: "))

canvas = tkinter.Canvas(width=canvas_width, height = canvas_height)
canvas.pack()


for i in range(pocet):
    x = random.randint(1,30)
    y = random.randint(1, canvas_width-3-x)
    z = random.randint(1, canvas_height-3-x)
    if x < 10:
        farba = "red"
    elif x < 20:
        farba = "green"
    elif x > 20:
        farba = "blue"


    canvas.create_rectangle(y, z, y+x, z+x, fill=farba, width=0)












tkinter.mainloop()