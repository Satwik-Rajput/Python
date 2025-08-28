s = open("file.txt")
'''
line1 = s.readline()
print(line1)
line2 = s.readline()
print(line2)
line3 = s.readline()
print(line3)
line4 = s.readline()
print(line4)'''
a = s.readline()
while(a!=""):
    print(a)
    a = s.readline()
s.close()