Word =["donkey" , "ganda" ,"bad"]
with open("donkey.txt")as f:
    contant = f.read()
    for word in Word:
        contant = contant.replace(word ,"#"*len(word))
    with open("donkey.txt","w")as f:
        f.write(contant)