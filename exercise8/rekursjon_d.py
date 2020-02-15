def binarySearch(numbers,element):
    if element not in numbers:
        return "Element not in list"
    index1 = int(len(numbers)/2)
    if element == numbers[index1]:
        return index1
    elif element < numbers[index1]:
        return binarySearch(numbers[:index1],element)
    else:
        return index1 + binarySearch(numbers[index1:],element)
print(binarySearch([1,4,6,9,13,34,45,53,65,78],78))