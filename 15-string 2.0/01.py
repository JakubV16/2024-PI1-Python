ret="Ahoj Svet"
ret1=ret[:6]
ret2=ret[5:]
print(ret1)
print(ret2)
# ret[5]='s'  # neni dovolene v pythone
novyret= ret[:5]+'s'+ ret[6:]
print(novyret)
novyret= novyret + ' svet'
print(novyret)
novyret=  3* novyret
print(novyret)