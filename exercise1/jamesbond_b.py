heltall = input("Oppgi heltallsdelen av tallet: ")
desimaler = input("Oppgi desimaldelen av tallet: ")
antalldesimaler = int(len(desimaler))
antalldesimaler_avrundet = int(input("Oppgi ønsket antall desimaler i avrunding: "))
desimaler_avrundet = int(round(int(desimaler),-(antalldesimaler-antalldesimaler_avrundet)))
print(int(heltall+str(desimaler_avrundet))/10**antalldesimaler)