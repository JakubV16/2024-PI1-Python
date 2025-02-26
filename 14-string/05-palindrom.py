#retazec ktory je rovnaký pri čítaní od začiatku alebo od konca ABBA
ret="ABBA"
obrateny = ret[::-1]
if ret==obrateny:
    print('Retazec', ret, 'je palindrom')

else:
    print('retazec',ret, 'nieje palindrom')