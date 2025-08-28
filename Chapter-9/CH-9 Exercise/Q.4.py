Word ="Donkey"
with open("donkey.txt")as f:
    contant = f.read()
    newcontent = contant.replace(Word ,"#####")
    with open("donkey.txt","w")as f:
        f.write(newcontent)