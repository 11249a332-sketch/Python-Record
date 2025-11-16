try:
    file = open("example.txt", "r")
    # Code to read from the file
except FileNotFoundError:
    print("File not found!")
else:
    print(file.read())
    file.close()

