class Auto:
    def __init__(self, znacka, farba, cena,rychlost,meno):
        self.znacka = znacka
        self.farba = farba
        self.cena = cena
        self.rychlost = rychlost
        self.meno = meno
        
    def vypis_info(self):
        print('\n******Tvoje Buduce Avto******')
        print(f'Zadaj svoje meno {self.meno}')
        print(f'znacka je {self.znacka}')
        print(f' farba bude{self.farba}')
        print(f'cena auta bude {self.cena}')
        print(f'max. rychlost je {self.rychlost}')

meno=input('Zadaj kto bude majitel auta:')
znacka=input('Zadaj tvoju  znacku auta:')
farba=input('Zadaj farbu tvojho auta:')
cena=input('Zadaj cenu tvojho auta:')
rychlost=input('Aká bude max rychlost tvojho auta:')

auto=Auto('meno','znacka','farba','cena','rychlost')
auto.vypis_info()