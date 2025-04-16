# string je retazec znakov napr. "Ahoj"
# retazec zaciname a koncime  "" alebo ''
# \n  = enter, nový riadok
# \t = tabulátor
# \ = vypíše ""
# funkcia len() = vráti dlzku retazca (pocet znakov)
# znaky v retazci sú indexované - prvý znak má index 0                                                       
# index píšeme do hranatých zatvoriek [] "Alt Gr + F"




retazec='Hello World'
print(retazec)
print(len(retazec))

for i in range(len(retazec)):
    print(retazec[i])


for znak in retazec:  # postupne vyberá znaky s retazca do premennej znak
    print(znak)