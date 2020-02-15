set1 = set()
for x in range(1,20,2):
    set1.add(x)
set2 = set()
for x in range(1,10,2):
    set2.add(x)
set3 = set1-set2
set4 = set2 & set3
def allUnique(list1):
    set1 = set()
    for x in list1:
        set1.add(x)
    if len(list1)==len(set1):
        return True
    else:
        return False
def removeDuplicates(list1):
    set1 = set()
    for x in list1:
        set1.add(x)
    return list(set1)
print(removeDuplicates([1,3,5,2,3,7]))