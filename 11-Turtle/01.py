import turtle
import random
t = turtle.Turtle()
turtle.bgcolor("black")
t.pos()
(0,0)
t.heading()
0
t.speed(0)

x=1
for i in range(150):
    t.pencolor(f"#{random.randrange(256**3):06x}")
    t.forward(x)
    t.right(90)
    x=x+5








turtle.mainloop()