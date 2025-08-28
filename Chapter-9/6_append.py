s = "\nAnd also he is good at coding."
f = open("my_file.txt","a")
f.write(s)
f.close()


# 2nd method
# using with statement
'''
with open("my_file.txt","a")as f:
    f.write("\nHe is a smart worker.")'''