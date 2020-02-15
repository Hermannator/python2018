tall = int(input("Skriv inn et positivt heltall: "))
heltall = tall
faktorer = []
for x in range(2,tall+1):
    while tall%x == 0:
        faktorer.append(x)
        tall = int(tall/x)
if len(faktorer)==1:
    print(f"{heltall} er et primtall.")
else:
    result = f"{heltall} = "
    for x in faktorer:
        result += f'{x}*'
    result = result[:-1]
    print(result)
