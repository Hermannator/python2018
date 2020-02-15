boligtype = input("Sekundærbolig eller fritidsbolig? ")

if boligtype == "Sekundærbolig":
    utleieinntekt = input("Oppgi utleieinntekten: ")
    print(f"Inntekten er skattepliktig.\nTotalt skattepliktig beløp er {utleieinntekt}.")
elif boligtype == "Fritidsbolig":
    formal = input("Primært brukt til fritid eller utleie? ")
    antall = int(input("Hvor mange fritidsboliger leier du ut? "))
    utleieinntekt = int(input("Oppgi utleieinntekt per fritidsbolig: "))
    if formal == "Fritid":
        skattegrunnlag = (antall * (utleieinntekt-10000))*0.85
    elif formal == "Utleie":
        skattegrunnlag = antall * utleieinntekt
    if skattegrunnlag>0:
        print(f"Inntekten er skattepliktig.\nTotalt skattepliktig beløp er {skattegrunnlag}.")
    else:
        print("Inntekten er skattefri.")
