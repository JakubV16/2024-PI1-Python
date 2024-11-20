import random # knižnica, ktorá slúži na generovanie náhodných hodnôt

nahodne_cislo = random.randint(0,36) # vygeneruje náhodné celé číslo z rozsahu 0...36
print(nahodne_cislo)

nahodna_farba = random.choice(["red", "green", "black"]) # vygeneruje náhodnú hodnotu so zoznamu hodnôt, zoznam ohraničíme takýmito zátvorkami[]
print(nahodna_farba)

nahodne_pismeno = random.choice("Ahoj")
print(nahodne_pismeno)