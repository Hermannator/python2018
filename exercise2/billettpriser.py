dager = int(input("Dager til du skal reise? "))
if dager>=14:
    minipris = input("Minipris 199,- kan ikke refunderes/endres.\nØnskes dette? (J/N) ")
else:
    minipris = "N"
student = input("Er du student? (J/N) ")
if minipris == "J":
    if student == "J":
        pris = 199 * 0.9
    else:
        pris = 199
elif minipris == "N":
    pris = 440
    if student == "J":
        pris = pris * 0.75
    alder = int(input("Din alder: "))
    if alder < 16 or alder >= 60:
        if alder < 16:
            pris = pris * 0.5
        if alder >= 60:
            pris = pris * 0.75
    else:
        militar = input("Er du i militæret? (J/N) ")
        if militar == "J":
            pris = pris * 0.75
print(f"Prisen på billetten blir: {pris},-")