import tkinter as tk
from PIL import Image, ImageTk
import random

# Vytvorenie hlavného okna
okno = tk.Tk()
okno.title("Pexeso – Tipos Extraliga")

# Zoznam obrázkov tímov (použije sa 2x každý)
timy = [
    "slovan.png",
    "kosice.png",
    "dukla.png",
    "nitra.png",
    "zvolen.png",
    "poprad.png",
    "zilina.png",
    "banskabystrica.png"
]

# Zduplikujeme obrázky (lebo v pexese je každý obrázok 2x) a premiešame
karty = timy * 2
random.shuffle(karty)

# Funkcia na načítanie a zmenšenie obrázku
def nacitaj_obrazok(subor):
    obrazok = Image.open(subor)
    obrazok = obrazok.resize((100, 100))  # prispôsobenie veľkosti
    return ImageTk.PhotoImage(obrazok)

# Načítame všetky obrázky vrátane zadnej strany karty
obrazky = {nazov: nacitaj_obrazok(nazov) for nazov in set(karty)}
zadna_strana = nacitaj_obrazok("zadna.png")

# Herné premenné
tlacidla = []
odhalene = []
stavy = [False] * 16  # ktoré sú už nájdené

# Funkcia po kliknutí na kartu
def klik(i):
    if stavy[i] or len(odhalene) == 2:
        return
    tlacidla[i].config(image=obrazky[karty[i]])
    odhalene.append(i)
    if len(odhalene) == 2:
        okno.after(1000, skontroluj)

# Skontrolujeme, či sa odhalené karty zhodujú
def skontroluj():
    i1, i2 = odhalene
    if karty[i1] == karty[i2]:
        stavy[i1] = True
        stavy[i2] = True
    else:
        tlacidla[i1].config(image=zadna_strana)
        tlacidla[i2].config(image=zadna_strana)
    odhalene.clear()

# Vytvorenie tlačidiel v mriežke 4x4 s malými medzerami
for i in range(16):
    btn = tk.Button(okno, image=zadna_strana, command=lambda i=i: klik(i))
    btn.grid(row=i//4, column=i%4, padx=5, pady=5)  # tu sú tie jemné medzery
    tlacidla.append(btn)

# Spustenie aplikácie
okno.mainloop()


