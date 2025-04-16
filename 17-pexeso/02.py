import tkinter as tk
import random


okno = tk.Tk()
okno.title("Moje Pexeso")


hodnoty = list("AABBCCDDEEFFGGHH")


random.shuffle(hodnoty)


tlacidla = []        
otocene = []         
uz_najdene = []      



def klik(i):
    
    if i in uz_najdene or i in otocene or len(otocene) == 2:
        return

    
    tlacidla[i]['text'] = hodnoty[i]
    otocene.append(i)

    
    if len(otocene) == 2:
        okno.after(1000, skontroluj)



def skontroluj():
    a, b = otocene

   
    if hodnoty[a] == hodnoty[b]:
        uz_najdene.extend([a, b])
    else:
        
        tlacidla[a]['text'] = ""
        tlacidla[b]['text'] = ""

    
    otocene.clear()



for i in range(16):
    btn = tk.Button(
        okno,
        text="",
        width=6,
        height=3,
        font=("Arial", 20),
        command=lambda i=i: klik(i)
    )

   
    tlacidla.append(btn)

    
    riadok = i // 4
    stlpec = i % 4
    btn.grid(row=riadok, column=stlpec, padx=10, pady=10)



okno.mainloop()