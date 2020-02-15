print("Dette er et program for å teste din sjenerøsitet.")
har_epler = int(input("Hvor mange epler har du? "))
if har_epler == 0:
   print("Æsj, det sier du bare for å slippe å gi noe!")
else:
    gir_epler = int(input("Hvor mange kan du gi til meg? "))
    if gir_epler < har_epler / 2:
        print("Du beholder det meste for deg selv...")
    else:
        print("Takk, det var snilt!")
    if abs(har_epler-gir_epler) == 1:
        eple = "eple"
        det = "det"
    else:
        eple = "epler"
        det = "de"
    if har_epler-gir_epler < 0:
        print(f'Du har nå 0 epler igjen. Gi meg {det} {abs(har_epler-gir_epler)} du skylder meg neste gang vi møtes.')
    else:
        print(f'Du har nå {har_epler - gir_epler} {eple} igjen.')