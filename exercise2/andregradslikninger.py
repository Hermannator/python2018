import math
a = float(input("ax^2+bx+c, gi a: "))
b = float(input("ax^2+bx+c, gi b: "))
c = float(input("ax^2+bx+c, gi c: "))
d = b**2-4*a*c
result = "Andregradslikningen "+str(a)+"x^2 + "+str(b)+"x + "+str(c)+" har "
if d<0:
    result += "to imaginære løsninger."
elif d>0:
    if b>=0:
        losning1 = (-b-math.sqrt(d))/(2*a)
        losning2 = (2*c)/(-b-math.sqrt(d))
    else:
        losning1 = (2*c)/(-b+math.sqrt(d))
        losning2 = (-b+math.sqrt(d))/(2*a)
    result += "de to reelle løsningene "+str(losning1)+" og "+str(losning2)+"."
else:
    losning = -b/(2*a)
    result += "den reelle dobbeltroten "+str(losning)+"."
print(result)