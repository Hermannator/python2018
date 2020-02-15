for x in range(1, 6):
    line = ""
    for y in range(1,6):
        line += str(y) + " "
        if y==x:
            break
    print(line)
