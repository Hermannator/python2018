def gcd(a,b):
    while b!=0:
        gammel_b=b
        b=a%b
        a=gammel_b
        gcd(a,b)
    return a
def reduce_fraction(a,b):
    d=gcd(a,b)
    return a/d,b/d
teller,nevner = reduce_fraction(8,12)
print(f"{int(teller)}/{int(nevner)}")