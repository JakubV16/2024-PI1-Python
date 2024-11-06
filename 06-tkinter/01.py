import tkinter

canvas = tkinter.Canvas()  # vytvorenie plátna a jeho priradenie do premennej canvas
canvas.pack()    # umiestnenie plátna do okna

canvas.create_text(100, 75, text="Ahoj")
# vypíše text "Ahoj" na pozícii x=100, y=100
# súradnice zadávame vždy v poradí x, y
# x rastie smerom doprava a y rastie smerom dole

canvas.create_rectangle(50, 50, 150, 100)
# vykreslenie štvorca (obdlžníka)
# prvé dve čísla určujú posíciu začiatočného bodu
# dalšie dve určujú pozíciu koncového bodu

canvas.create_oval(50, 50, 150, 100)
# vykreslenie kruhu (ovalu)
# prvé dve čísla určujú posíciu začiatočného bodu
# dalšie dve určujú pozíciu koncového bodu

tkinter.mainloop() # aby ostalo okno otvorené, aby sa nezavrelo