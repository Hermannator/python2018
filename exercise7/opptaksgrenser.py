f=open("poenggrenser_2011.csv","r")
opptaksgrenserList = (f.read()).split("\n")
f.close()
opptaksgrenserDict = {}
for x in opptaksgrenserList:
    if x.strip():
        x = x.strip("\n ' '")
        x = x.split(",")
        x[0] = x[0].strip('"')
        x[1] = x[1].strip('"')
        if x[1] != 'Alle':
            x[1] = float(x[1])
        opptaksgrenserDict[x[0]]=x[1]
def apneStudier():
    antallAlle = 0
    for x in opptaksgrenserDict:
        if opptaksgrenserDict[x] == '"Alle"':
            antallAlle += 1
    return antallAlle
def snittNTNU():
    antallStudier = 0
    poengSum = 0
    for x in opptaksgrenserDict:
        if x[0:4] == "NTNU":
            if opptaksgrenserDict[x]!="Alle":
                antallStudier += 1
                poengSum += opptaksgrenserDict[x]
    snitt = round(poengSum/antallStudier,2)
    return snitt
def lavesteSnitt():
    nedreGrense = 100
    lavesteStudie = ""
    for x in opptaksgrenserDict:
        if opptaksgrenserDict[x] != "Alle":
            if opptaksgrenserDict[x] < nedreGrense:
                nedreGrense = opptaksgrenserDict[x]
                lavesteStudie = x
    return lavesteStudie
def removeDuplicates(list1):
    set1 = set()
    for x in list1:
        set1.add(x)
    return list(set1)
skolenavn = []
for x in opptaksgrenserDict:
    x = x.split(" ")
    if x[0] not in skolenavn:
        skolenavn.append(x[0])
studieoversikt = {}
for y in skolenavn:
    studieoversikt[y] = []
    for x in opptaksgrenserDict:
        if (x.split(" "))[0] == y:
            studie = {}
            studie[(x.split(" "))[2]] = opptaksgrenserDict[x]
            studieoversikt[y].append(studie)
for x in studieoversikt:
    print(f"{x} {studieoversikt[x]}")