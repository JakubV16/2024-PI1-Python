import tkinter
import random



vklad = int(input("Zadaj svoj vklad:"))



canvas = tkinter.Canvas(width=1500, height=900)
canvas.pack()


canvas.create_oval(50, 50, 600, 600, fill="sienna")
canvas.create_oval(65, 65, 585, 585, fill="white")
canvas.create_oval(200, 200, 450, 450, fill="saddlebrown")
canvas.create_oval(130, 130, 520, 520)
canvas.create_oval(310, 310, 340, 340, fill="gold")
















tkinter.mainloop()
