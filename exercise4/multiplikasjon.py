def multiplikasjon(tol):
    prod = 1
    count = 0
    change = 2
    while change>tol:
        count += 1
        oldprod = prod
        prod *= 1+1/(count**2)
        change = prod - oldprod
    return [prod,count]
tol = float(input("tol = "))
print(f"Produktet ble {round(multiplikasjon(tol)[0],2)} etter {multiplikasjon(tol)[1]} iterasjoner.")