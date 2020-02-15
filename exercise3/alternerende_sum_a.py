n = int(input("n = "))
tallseriesum = 0
for x in range(1,n+1):
    if x%2==0:
        tallseriesum -= x**2
    else:
        tallseriesum += x**2
print(f"Summen av tallserien er {tallseriesum}.")