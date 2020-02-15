andel = int(input("Oppgi hvor mye av boligen som ble utleid, i prosent: "))
leieinntekt = int(input("Oppgi leieinntekten: "))
if andel>=50:
    if leieinntekt>=20000:
        print(f"Inntekten er skattepliktig.\nSkattepliktig beløp er {leieinntekt} kr.")
    else:
        print("Inntekten er skattefri.")
else:
    print("Inntekten er skattefri.")