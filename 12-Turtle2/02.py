import turtle

t=turtle.Turtle()
pocet=4
dlzka=50


def domy(pocet, dlzka):
    for i in range(pocet):
        t.pensize(4)
        t.fillcolor("red")
        t.begin_fill()
        t.forward(dlzka)
        t.right(90)
        t.forward(dlzka)
        t.right(90)
        t.forward(dlzka) 
        t.right(90)
        t.forward(dlzka)
        t.right(90)
        t.end_fill()
        t.fillcolor("black")
        t.begin_fill()
        t.left(45)
        t.forward(35)
        t.right(90)  
        t.forward(35)
        t.penup()
        t.left(45)
        t.forward( dlzka)
        t.pendown()
        t.end_fill()
        




domy(pocet, dlzka)

dokno=28
t.pensize(3)
t.penup()
t.right(180)
t.forward(8*dlzka)
t.left(90)
t.forward(12)
t.left(90)
t.forward(12)
t.pendown()

def okna(pocet, dokno):
    for i in range(pocet):
        t.fillcolor("blue")
        t.begin_fill()
        t.forward(dokno)
        t.right(90)
        t.forward(dokno)
        t.right(90)
        t.forward(dokno)
        t.right(90)
        t.forward(dokno)
        t.right(90)
        t.forward(dokno/2)
        t.right(90)
        t.forward(dokno)
        t.right(90)
        t.forward(dokno/2)
        t.right(90)
        t.forward(dokno/2)
        t.right(90)
        t.forward(dokno)
        t.left(90)
        t.forward(dokno/2)
        t.right(90)
        t.penup()
        t.forward(72)
        t.pendown()
        t.end_fill()
        




okna(pocet, dokno)







turtle.mainloop()