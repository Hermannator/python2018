k = int(input("k = "))
tallseriesum = 0
ledd = 0
def tallserie(n):
    tallseriesum = 0
    for x in range(1, n + 1):
        if x % 2 == 0:
            tallseriesum -= x ** 2
        else:
            tallseriesum += x ** 2
    return tallseriesum
while tallseriesum <= k:
    ledd += 1
    tallseriesum = tallserie(ledd)
print(f"Summen av tallene før summen blir større enn {k} er {tallserie(ledd-1)}. Antall iterasjoner: {ledd-1}.")