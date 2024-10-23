# výpis párnych čísiel
cislo = int(input("Zadaj číslo:"))
print(f"Párne čísla do {cislo}:")
for i in range(2, cislo+1, 2):
    print(i)
# výpis nepárnych čísiel   
print(f"Nepárne čísla do {cislo}:")
for i in range(1, cislo+1, 2):
    print(i)

if cislo % 2 == 0:
    print(f"Číslo {cislo} je párne.")
else:
    print(f"Číslo {cislo} je nepárne.")