x = int(input("Aký typ príkladu chceš?(1,2)"))
if x == 1:
    a = int(input("Zadaj prvé číslo príkladu: ")) 
    b = int(input("Zadaj druhé číslo príkladu: ")) 
    sucet = a + b
    print("Súčet je: ", sucet)
    sucin = a * b
    print("Súčin je: ", sucin)
    rozdiel = a - b
    print("Rozdiel je: ", rozdiel)
    podiel = a / b 
    print("Podiel je: ", podiel)
    druhamocninaa = a * a
    print ("Druhá mocnina prvého čísla je :", druhamocninaa)
    druhamocninab = b * b
    print ("Druhá mocnina druhého čísla je :", druhamocninab)
    tretiamocninaa = a * a * a
    print ("Tretia mocnina prvého čísla je :", tretiamocninaa)
    tretiamocninab = b * b * b
    print ("Tretia mocnina druhého čísla je :", tretiamocninab)

elif x == 2:
    a = int(input("Zadaj prvé číslo príkladu: ")) 
    b = int(input("Zadaj druhé číslo príkladu: ")) 
    c = int(input("Zadaj tretie číslo príkladu: ")) 
    sucet = a + b + c
    print("Súčet je: ", sucet)
    sucin = a * b * c 
    print("Súčin je: ", sucin)
    rozdiel = a - b - c
    print("Rozdiel je: ", rozdiel)
    podiel = a / b / c
    print("Podiel je: ", podiel)
    druhamocninaa = a * a
    print ("Druhá mocnina prvého čísla je :", druhamocninaa)
    druhamocninab = b * b
    print ("Druhá mocnina druhého čísla je :", druhamocninab)
    druhamocninac = c * c
    print ("Druhá mocnina tretieho čísla je :", druhamocninac)
    tretiamocninaa = a * a * a
    print ("Tretia mocnina prvého čísla je :", tretiamocninaa)
    tretiamocninab = b * b * b
    print ("Tretia mocnina druhého čísla je :", tretiamocninab)
    tretiamocninac = c * c * c
    print ("Tretia mocnina tretieho čísla je :", tretiamocninac)
    miesanie1 = a + b * c
    print("Sučet prvého a druhého a súčin druhého a tretieho čísla je:", miesanie1 )
    miesanie2 = a * b + c
    print("Súčin prvého a druhého a súčet druhého a tretieho čísla je:", miesanie2 )
    miesanie3 = a * c + b
    print("Súčin prvého a tretieho a súčet druhého a tretieho čísla je:", miesanie3 )








