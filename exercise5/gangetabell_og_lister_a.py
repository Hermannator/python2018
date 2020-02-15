def separate(numbers,threshold):
    liste1 = numbers[:threshold-1]
    liste2 = numbers[threshold-1:]
    return liste1,liste2

numbers = [1,2,3,4,5,6,7,8]
liste1,liste2 = separate(numbers,7)
print(liste1)
print(liste2)