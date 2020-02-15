h = int(input("Skriv inn en høyde: "))
a = (3/(6**0.5))*h
areal = (3**0.5)*(a**2)
volum = ((2**0.5)*(a**3))/12
print(f'Et tetraheder med høyde {h} har volum {round(volum, 2)} og areal {round(areal, 2)}.')