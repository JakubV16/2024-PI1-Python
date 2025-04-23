subor= open('subor.txt', 'r')
# otvorí súbot subor.txt na čítanie, pre zápis sa používa 'w'- write , 'r'- read ak súbor neexistuje vypíše chybu 
# subor= open('../subor.txt', 'r') .. je o priečinok vyššie

# for i in range (4):
#     riadok = subor.readline()
#     print (riadok)


# riadok=subor.readline()
# while riadok !='':
#     print(riadok)
#     riadok=subor.readline()

while True:
    riadok=subor.readline()
    if riadok=='':
        break
    print(riadok.strip())

subor.close()  # zatvorí súbor 