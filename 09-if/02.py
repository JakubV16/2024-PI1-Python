import tkinter
import random

pocet = int(input("Zadaj počet kruhov: "))
canvas_width = int(input("Zadaj šírku plátna: "))
canvas_height = int(input("Zadaj výšku plátna: "))

canvas = tkinter.Canvas(width=canvas_width, height = canvas_height)
canvas.pack()

for i in range(pocet):
     y = random.randint(5, canvas_width-15)
     z = random.randint(5, canvas_height-15)
#     if y<=canvas_width/2 and z<=canvas_height/2:
#         farba="blue"
#     elif y>=canvas_width/2 and z>=canvas_height/2:
#         farba="yellow"
#     elif y>=canvas_width/2 and z<=canvas_height/2:
#         farba="red"
#     elif y<=canvas_width/2 and z>=canvas_height/2:
#         farba="green"

if z<canvas_width/2:
    if y<canvas_height/2:
        farba="blue"
    else:
        farba="lime"
else:
    if z<canvas_height/2:
        farba="red"
    else:
        farba="yellow"
    canvas.create_oval(y, z, y+10, z+10, fill=farba)



tkinter.mainloop()