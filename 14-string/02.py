
retazec = (input("Zadaj slovo: "))

print("Dlžka retazca je",len(retazec),"znakou ")
print()

for i in range(len(retazec)):
    print(retazec[i])
   

for j in range(len(retazec)):
    print(retazec[-j -1])
print() 

for znak in retazec:
    print(znak*3)