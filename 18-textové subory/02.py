subor= open('subor2.txt', 'r')

while True:
    riadok=subor.readline()
    if riadok=='':
        break
    print(riadok.strip())

subor.close()  # zatvorí súbor 