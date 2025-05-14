import tkinter
import random

canvas = tkinter.Canvas(width=800, height=800)
canvas.pack()

file=open('tvary.txt', 'w')
riadok=[]
# ftvary=open('tvary.txt', 'w' )
tvary=random.choice('ORL')
riadok.append(tvary)
print(tvary)

for i in range(4):
    suradnice=random.randint(3,797)
    riadok.append(suradnice)
    print(suradnice)

for i in range(3):
    farba=random.randint(0,255)
    riadok.append(farba)
    print(farba)

print(riadok)










tkinter.mainloop()