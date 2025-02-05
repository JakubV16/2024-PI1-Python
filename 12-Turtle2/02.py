import turtle

t=turtle.Turtle()
pocet=4
dlzka=50

def domokno(pocet, dlzka):
    for i in range(pocet):
        t.fillcolor('red')
        t.begin_fill()
        t.forward(dlzka)
        t.right(90)
        t.forward(dlzka)
        t.right(90)
        t.forward(dlzka)
        t.right(90)
        t.forward(dlzka)
        t.end_fill()
        t.fillcolor('black')
        t.begin_fill()
        t.right(45)
        t.forward(35)
        t.right(90)
        t.forward(35)
        t.right(45)
        t.end_fill()
        t.penup()
        t.forward(38)
        t.right(90)
        t.forward(12)
        t.pendown()
        t.fillcolor('blue')
        t.begin_fill()
        t.forward(dlzka/2)
        t.right(90)
        t.forward(dlzka/4)
        t.right(90)
        t.forward(dlzka/2)
        t.left(90)
        t.forward(dlzka/4)
        t.left(90)
        t.forward(dlzka/2)
        t.left(90)
        t.forward(dlzka/2)
        t.left(90)
        t.forward(dlzka/2)
        t.left(90)
        t.forward(dlzka/4)
        t.left(180)
        t.forward(dlzka/4)
        t.right(90)
        t.forward(dlzka/4)
        t.right(90)
        t.forward(dlzka/2)
        t.end_fill()
        t.penup()        
        t.right(90)
        t.forward(dlzka)
        t.left(90)
        t.forward(dlzka/4)
        t.right(90)
        t.pendown()





domokno(pocet, dlzka)




turtle.mainloop()