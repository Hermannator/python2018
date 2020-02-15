def karakterer():
    streng = "Discworld"
    for x in streng:
        print(x)

def tredjebokstav(streng):
    try:
        return streng[2]
    except:
        return "q"
print(tredjebokstav("discworld"))

def biggestIndex(streng):
    index = 0
    while True:
        try:
            streng[index]
        except:
            return index-1
        index+=1
print(biggestIndex("The Way of Kings"))