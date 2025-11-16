import os.path
import sys
fname = input("Enter the filename:")
if not os.path.isfile(fname):
    print("File",fname," does not exist")
    sys.exit(0)
infile = open(fname, "r")
linelist = infile.readline()
linecount = int(input("Enter the number of lines in the file:"))
for i in range(linecount):
    print(i+1,":",linelist[i], end="")
word=input("\nEnter the word:")
cnt = 0
for line in linelist:
    cnt += line.count(word)
print("The word", word, "appears", cnt, "times in the file")