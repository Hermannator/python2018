myFamily = {}
def addFamilyMember(role,name):
    if role not in myFamily:
        myFamily[role] = []
    myFamily[role].append(name)
addFamilyMember("bror","Arne")
addFamilyMember("mor","Anne")
addFamilyMember("bror","Geir")
for x in myFamily:
    line = f"{x}: "
    for y in myFamily[x]:
        line += f"{y}, "
    print(line[:-2])