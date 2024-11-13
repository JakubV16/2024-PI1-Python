import tkinter

canvas = tkinter.Canvas(width=600, height=600)
canvas.pack()

def xko(x, y):  # definicia funkcie, xko názov (to dávame my), ()sú takzvané parametre funkcie

    canvas.create_rectangle(x, y, x+10, y+10, outline="white", fill="black")
    canvas.create_rectangle(x, y+10, x+10, y+20, outline="white", fill="black")
    canvas.create_rectangle(x+10, y+20, x+20, y+30, outline="white",fill="black")
    canvas.create_rectangle(x+20, y+30, x+30, y+40, outline="white", fill="black")
    canvas.create_rectangle(x+10, y+40, x+30, y+50, outline="white", fill="black")
    canvas.create_rectangle(x, y+50, x+40, y+60, outline="white", fill="black")
    canvas.create_rectangle(x, y+60, x+10, y+70, outline="white", fill="black")
    canvas.create_rectangle(x+30, y+20, x+40, y+30, outline="white", fill="black")
    canvas.create_rectangle(x+30, y+40, x+40, y+50, outline="white", fill="black")
    canvas.create_rectangle(x+40, y, x+50, y+10, outline="white", fill="black")
    canvas.create_rectangle(x+40, y+10, x+50, y+20, outline="white", fill="black")
    canvas.create_rectangle(x+40, y+50, x+50, y+60, outline="white", fill="black")
    canvas.create_rectangle(x+40, y+60, x+50, y+70, outline="white", fill="black")
def riadok_x(x, y, pocet):
    for i  in range(pocet):
        xko(x, y)
        x+=60

def riadky_x(x, y, pocet_riadkov, pocet_stlpcov):
    for i in range(pocet_riadkov):
        riadok_x(x, y, pocet_stlpcov)
        y+=80
    


# xko(10, 10) #volanie funkcie, na tomto mieste sa vykoná
# xko(70, 10)
# xko(130, 10) 

# x=10
# y=10
# for i in range(3):
#     pocet=5
#     for i in range(pocet):
#         xko(x, y)
#         x=x+60
#     x=10
#     y=y+80

xko(10, 10)
riadok_x(10, 100, 3,)
riadky_x(10, 190, 3, 3) 

tkinter.mainloop()