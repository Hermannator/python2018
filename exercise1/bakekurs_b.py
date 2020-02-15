a = input('Hvor mange cookies vil du lage?')
b = input('og hvor mange cookies vil du lage nå?')
c = input('og hvor mange cookies vil du lage til slutt?')
abc = [a,b,c]
print('Antall cookies:'.ljust(15) + 'sukker(g)'.rjust(15) + 'sjokolade(g)'.rjust(25))
for x in abc:
    sukker = str(round(((int(x))/48*400),1))
    sjokolade = str(round(((int(x))/48*500),1))
    print(x.ljust(15) + sukker.rjust(15) + sjokolade.rjust(25))
