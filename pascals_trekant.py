def factorial_loop(n):
    p = 1
    for i in range(1, n + 1):
        p *= i

    return p

def nchoosek(n,k):
    return int(factorial_loop(n)/(factorial_loop(k)*factorial_loop(n-k)))

def pascal(n):
    linjeliste = []
    for i in range(n):
        linje = ""
        for j in range(i + 1):
            linje += f'{nchoosek(i,j)} '
        linjeliste.append(linje)
    for linje in linjeliste:
        print(linje.center(len(linjeliste[n-1])))
pascal(int(input("Antall linjer: ")))