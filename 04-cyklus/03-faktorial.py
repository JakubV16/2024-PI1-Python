n = int(input("Zadaj n: "))
faktorial = 1
for i in range(n):
    print(i+1)
    faktorial = faktorial * (i+1)
    print(i, i+1, faktorial)
# print(n , "! =",faktorial)
print(f"{n}!={faktorial}") # {} napíšeme pravý alt+b