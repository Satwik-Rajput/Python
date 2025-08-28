with open("file.txt") as f:
    data = f.read()
with open("newfile.txt","w") as f:
    f.write(data)