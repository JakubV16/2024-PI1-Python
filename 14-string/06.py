#string v pythone je immutable nezmenuiteľný
ret = 'Ahoj Svet'
#ret[0]='a'  #toto nie je možne lebo to je immutrable
ret='a'+ret[1:]     # ak chceme zmeniť nejaký znak musíme to urobiť takto
print(ret)


# retazce vieme porovnavat

print('a'=='b')
print(ord("a")) # ord () je funkcia ktorá vráti ordinálnu číselnu hodnotu znaku
print(ord('A'))
print('a'=='A')
print(chr(64))  # chr() je funkcia ktorá na zaklade ordinalnej hodnoty vrati znak