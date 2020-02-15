def checkEqual(str1,str2):
    if str1==str2:
        return True
    else:
        return False
def reversedWord(str1):
    str_list = list(str1)
    for x in range(int(len(str_list)/2)):
        current = str_list[x]
        str_list[x] = str_list[len(str_list)-1-x]
        str_list[len(str_list)-1-x] = current
    return "".join(str_list)
def checkPalindrome(str1):
    return checkEqual(str1,reversedWord(str1))
def containsString(str1,str2):
    try:
        for x in range(len(str1)):
            word = ""
            for y in range(len(str2)):
                if str1[x+y] == str2[y]:
                    word += f"{str1[x+y]}"
                if word == str2:
                    return x
    except:
        return -1
print(containsString("cocacola","ola"))