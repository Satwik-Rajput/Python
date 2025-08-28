f = open('file.txt')
s = f.readlines()
print(s,type(s))
f.close()

# 2nd method using with statement.
'''
with open("file.txt")as f:
    print(f.readlines(),type(f.readlines()))
    '''