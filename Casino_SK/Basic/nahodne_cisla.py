import random

cislo = int(input("Typni si číslo: "))

nahodne_cislo = random.randint(1,30)
if cislo in range(1, 31):
    if cislo == nahodne_cislo:
        print("Trafil si sa!")
    else:
        print(f"Bohužiaľ, správne číslo bolo {nahodne_cislo}!")
else:
    print("Také číslo tu nieje!")

