import random
import math
def makeVec():
    a = random.randint(-10,10)
    b = random.randint(-10,10)
    c = random.randint(-10,10)
    return [a,b,c]
def vectorPrint(vec,vecName):
    print(f"{vecName} = {vec}")
def skalarProdukt(vec,skalar):
    product = []
    for x in vec:
        product.append(x*skalar)
    return product
def vecLen(vec):
    l = 0
    for x in vec:
        l += x**2
    return math.sqrt(l)
def prikkProdukt(vec1,vec2):
    product = 0
    for x in range(len(vec1)):
        product += vec1[x]*vec2[x]
    return product
def main():
    vec1 = makeVec()
    vectorPrint(vec1,"vec1")
    skalar = int(input("Skalar: "))
    skalarProdukt1 = skalarProdukt(vec1, skalar)
    lengde1 = vecLen(vec1)
    lengde2 = vecLen(skalarProdukt1)
    print(f"Lengde før skalering: {round(lengde1,2)}")
    print(f"Lengde etter skalering: {round(lengde2,2)}")
    print(f"Forhold mellom lengdene: {int(lengde2/lengde1)}")
    print(f"Prikkproduktet mellom {vec1} og {skalarProdukt1}: {prikkProdukt(vec1,skalarProdukt1)}")
main()