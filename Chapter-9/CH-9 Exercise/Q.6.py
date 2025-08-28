with open("log.txt") as f:
    contant = f.read()
    if("python" in contant):
        print("Yes, pthon is in contant.")
    else:
        print("No, python is not in contant.")