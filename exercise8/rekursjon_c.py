def find_smallest_element(numbers):
    if len(numbers)==1:
        return numbers[0]
    else:
        num1 = find_smallest_element(numbers[1:])
        num2 = numbers[0]
        if num2 < num1:
            num1 = num2
        return num1
print(find_smallest_element([5,3,2,6]))