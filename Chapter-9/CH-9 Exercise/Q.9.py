with open("file1.txt") as f:
    contant1 = f.read()

with open("file2.txt") as f:
    contant2 = f.read()

if (contant1==contant2):
    print("The files are identical")
else:
    print("The files are not identical")