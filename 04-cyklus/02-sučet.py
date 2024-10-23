n = int(input("Zadaj n: "))
sucet = 0
for i in range(n):
    print(i+1)
    sucet = sucet + (i+1) # sucet + (i+1) je výraz, najskôr sa vypočíta výraz a výsledná hodnota sa priradí do premennej
    print(i, i+1, sucet)
print("Súčet prvých", n , "čísel je", sucet)