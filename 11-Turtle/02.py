import turtle
import random

t = turtle.Turtle()             # premennej t priradíme vlastnosti turtle

dlzka=50
def stvorec (d):
    for i in range(4):
        t.forward (d)
        t.left(90)
def pismenoj():
    for i in range(3):
        stvorec(dlzka)
        t.fd(dlzka)

    t.fd(dlzka*-2)


pismenoj()

def pismeno():
    for i in range(5):
        stvorec(dlzka)
        t.fd(dlzka)

t.rt(90)


pismeno()


t.rt(90)

def pismenko():
    for i in range(2):
        stvorec(dlzka)
        t.fd(dlzka)


pismenko()

t.rt(90)

stvorec(dlzka)
t.fd(dlzka)









turtle.mainloop()