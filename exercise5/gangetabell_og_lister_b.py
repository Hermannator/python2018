def multiplication_table(n):
    tabell = []
    for x in range(1,n+1):
        rad = []
        for y in range(1,n+1):
            rad.append(y*x)
        tabell.append(str(rad))
    return "\n".join(tabell)
print(multiplication_table(4))