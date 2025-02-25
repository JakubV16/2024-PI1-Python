import tkinter
canvas= tkinter.Canvas(width=900, height=800)
canvas.pack()

canvas.create_rectangle(50, 50, 100 , 100, fill= "white") #A8

canvas.create_rectangle(100, 50, 150 , 100, fill= "sienna") #B8

canvas.create_rectangle(150, 50, 200 , 100, fill= "white") #C8

canvas.create_rectangle(200, 50, 250 , 100, fill= "sienna") #D8

canvas.create_rectangle(250, 50, 300 , 100, fill= "white") #E8

canvas.create_rectangle(300, 50, 350 , 100, fill= "sienna") #F8

canvas.create_rectangle(350, 50, 400 , 100, fill= "white") #G8

canvas.create_rectangle(400, 50, 450 , 100, fill= "sienna") #H8

canvas.create_rectangle(50, 100, 100 , 150, fill= "sienna") #A7

canvas.create_rectangle(100, 100, 150 , 150,fill= "white" ) #B7

canvas.create_rectangle(150, 100, 200 , 150, fill= "sienna") #C7

canvas.create_rectangle(200, 100, 250 , 150,fill= "white" ) #D7

canvas.create_rectangle(250, 100, 300 , 150, fill= "sienna") #E7

canvas.create_rectangle(300, 100, 350 , 150,fill= "white" ) #F7

canvas.create_rectangle(350, 100, 400 , 150,fill= "sienna"  ) #G7

canvas.create_rectangle(400, 100, 450 , 150, fill= "white") #H7



tkinter.mainloop()