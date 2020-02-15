import random
maks = 5
forsok = 3
antallriktige = 0
def gangetabell(faktor1,faktor2):
    global maks, forsok, antallriktige
    riktigsvar = faktor1 * faktor2
    svar = int(input(f"Hva blir {faktor1}*{faktor2}?"))
    if svar == riktigsvar:
        antallriktige += 1
        forsok = 3
        if antallriktige == 5:
            maks += 5
            antallriktige = 0
        print("Gratulerer, det er helt riktig!")
        nyrunde = input("Er det ønskelig med flere spørsmål? Skriv 1 for ja eller 0 for nei: ")
        if nyrunde == "1":
            gangetabell(random.randint(0, maks), random.randint(0, maks))
    else:
        forsok -= 1
        if forsok == 0:
            print("Du har brukt opp alle forsøkene dine.")
        else:
            print(f"Dessverre ikke riktig. Du har {forsok} forsøk igjen.")
            gangetabell(faktor1, faktor2)
gangetabell(random.randint(0,maks),random.randint(0,maks))
