import random
numbers = []
for x in range(34):
    numbers.append(x + 1)
def drawNumbers(n):
    numberList = []
    for x in range(n):
        numberList.append(numbers[random.randint(0,len(numbers)-1)])
    return numberList
def compList(list1,list2):
    antallLike = 0
    for x in list1:
        for y in list2:
            if x == y:
                antallLike += 1
    return antallLike
def winnings(antallRette,antallTillegg):
    if antallRette == 7:
        return 2749455
    if antallRette == 6:
        if antallTillegg > 0:
            return 102110
        else:
            return 3385
    if antallRette == 5:
        return 95
    if antallRette == 4 and antallTillegg > 0:
        return 45
    else:
        return 0
def main():
    #myGuess = []
    #for x in range(7):
    #    myGuess.append(int(input(f"Gjett {x+1}. tall: ")))
    myGuess = [24,2,5,31,6,17,14]
    lottotall = drawNumbers(7)
    tilleggstall = drawNumbers(3)
    antallRette = compList(myGuess,lottotall)
    antallTillegg = compList(myGuess,tilleggstall)
    vinning = winnings(antallRette,antallTillegg)
    return vinning-5
totalVinning = 0
for x in range(999999):
    totalVinning += main()
print(totalVinning)
