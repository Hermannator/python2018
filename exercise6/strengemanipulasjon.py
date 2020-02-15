def replaceString(str1,str2,str3):
    product = list(str1)
    str1 = list(str1)
    for x in range(len(str1)):
        word = ""
        for y in range(len(str2)):
            try:
                if str1[x+y].lower() == str2[y].lower():
                    word += f"{str1[x+y]}"
                if word.lower() == str2.lower():
                    product[x]=str3
                    for y in range(1,len(str2)):
                        product.pop(x+y)
                        str1.pop(x+y)
            except:
                continue
    return "".join(product)
print(replaceString("Is this the real life? Is this just fantasy?","iS","cool"))