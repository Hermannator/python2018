for x in range(1, 6):
    line = ""
    for y in range(1,6):
        if y == 1:
            line += "# "
        else:
            line += " "
        if y==x:
            line += "# "
            break
    print(line)
