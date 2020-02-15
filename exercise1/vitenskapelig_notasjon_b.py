melodilinjer = int(input("Antall ulike 10-toners melodilinjer du har hørt? "))
prosent = (melodilinjer/8.25e19)*100
print(f'Du har hørt {format(prosent,".1e")} prosent av mulige melodier.')