k = int(input("Velg k: "))
fibonacci = ["0", "1"]
forrigeForrigeTall = 0
forrigeTall = 1
if k==0:
    fibonacci = "0"
else:
    for x in range(0,k-1):
        svar = forrigeTall + forrigeForrigeTall
        fibonacci.append(str(svar))
        forrigeForrigeTall = forrigeTall
        forrigeTall = svar
fibonacciSum = 0
for x in fibonacci:
    fibonacciSum += int(x)
print(f'Fibonacci-rekken fram til og med f({k}): {", ".join(fibonacci)}.')
print(f"Summen av alle tallene til og med f({k}): {fibonacciSum}.")