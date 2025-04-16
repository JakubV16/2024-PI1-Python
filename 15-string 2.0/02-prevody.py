# print(bin(255)) # vypise cislo v binarnej podobe
# print(hex(255)) # vypise cislo v hexadecimalnej podobe
# print(0b11111111) # vypise binarne cislo v desiatkovej podobe
# print(0xff) # vypise hexadecimalne cislo v desiatkovej podobe

def dec_bin (cislo):
    binarne = ''
    while cislo > 0:
        zvysok = cislo % 2
        binarne = str(zvysok) + binarne
        cislo = cislo // 2
    return binarne

def dec_hex(cislo):
    hexadecimalne =''
    while cislo>0:
        zvysok= cislo % 16
        hexadecimalne= str(zvysok)+hexadecimalne
        if zvysok == 10:
            hexadecimalne= 'A'+ hexadecimalne
        elif zvysok == 11:
            hexadecimalne= 'B'+ hexadecimalne
        elif zvysok == 12:
            hexadecimalne= 'C'+ hexadecimalne
        elif zvysok == 13:
            hexadecimalne= 'D'+ hexadecimalne
        elif zvysok == 14:
            hexadecimalne= 'E'+ hexadecimalne
        elif zvysok==15:
            hexadecimalne= 'F'+ hexadecimalne 
        cislo= cislo //16
        
    return hexadecimalne


cislo = 11
print(ord('A'))
print(chr(65))
print(ord('B'))
print(dec_bin(cislo))
print(dec_hex(cislo))