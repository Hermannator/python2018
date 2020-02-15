def writeToFile(data):
    f=open("my_file.txt","w")
    f.write(f"{data}")
    f.close()
def readFromFile(filename):
    f=open(filename,"r")
    content = f.read()
    print(content)
    f.close()
def main():
    choice = input("Do you want to read or write?").lower()
    if choice == "done":
        return
    elif choice == "write":
        writeToFile(input("What do you want to write to file?"))
    elif choice == "read":
        try:
            readFromFile("my_file.txt")
        except:
            writeToFile("")
            readFromFile("my_file.txt")
    main()
main()