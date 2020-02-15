import math

tall = input('Gi inn et desimaltall: ')
tall_utenkomma = tall.split('.')
tall_str = tall_utenkomma[0] + tall_utenkomma[1]
tall_bak_komma = len(tall_utenkomma[1])
desimaler = int(input('Antall desimaler i avrunding: '))
if int(tall_str[len(tall_str)-tall_bak_komma+desimaler]) >= 5:
    avrundet = math.ceil((int(tall_str)/10))
else:
    avrundet = math.floor((int(tall_str)/10))
result = avrundet / (10**(desimaler))
print(f'Avrundet til {desimaler} desimaler: {result}.')