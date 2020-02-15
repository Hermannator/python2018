fasit = list((input("Skriv inn det hemmelige ordet: ")).lower())
liv = int(input("Hvor mange forsøk får brukeren? "))
maskertOrd = []
for x in fasit:
    maskertOrd.append("*")
while True:
    bokstavnr = 0
    if maskertOrd == fasit:
        print(f"Du gjettet ordet {''.join(fasit)} riktig, med {liv} liv igjen!")
        break
    riktig = False
    gjettet = input("Gjett en bokstav: ")
    for x in fasit:
        if gjettet == x:
            maskertOrd[bokstavnr] = x
            riktig = True
        bokstavnr += 1
    if riktig:
        print(f"Stemmer, bokstaven {gjettet} er i ordet: {''.join(maskertOrd)}")
    else:
        liv -= 1
        print(f"Bokstaven {gjettet} er ikke i ordet. Du har {liv} liv igjen.")
        if liv == 0:
            break
