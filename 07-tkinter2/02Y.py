import tkinter

canvas = tkinter.Canvas(width=320, height=320)
canvas.pack()

def yko(x, y):
    canvas.create_rectangle(x, y, x+10, y+10, fill="black")
    canvas.create_rectangle(x, y+10, x+10, y+20, fill="black")
    canvas.create_rectangle(x+10, y+20, x+20, y+30, fill="black")
    canvas.create_rectangle(x+20, y+30, x+30, y+40, fill="black")
    canvas.create_rectangle(x+20, y+40, x+30, y+50, fill="black")
    canvas.create_rectangle(x+20, y+50, x+30, y+60, fill="black")
    canvas.create_rectangle(x+20, y+60, x+30, y+70, fill="black")
    canvas.create_rectangle(x+30, y+20, x+40, y+30, fill="black")
    canvas.create_rectangle(x+40, y, x+50, y+10, fill="black")
    canvas.create_rectangle(x+40, y+10, x+50, y+20, fill="black")     
yko(10, 10) 
def riadok_y(x, y, pocet):
    for i in range(pocet):
        yko(x, y)
        x+=50



tkinter.mainloop()