with open("poem.txt")as p:
    s = p.read()
    # print(s)
    if "twinkle" in s:
        print("Yes,The word Twinkle is present in the file.")
    else:
        print("No,The word Twinkle is not present in the file.")