s = "Satwik singh is a very talented person."
f = open("my_file.txt","w")
f.write(s)
f.close()

# 2nd method to write a file
'''
with open("my_file.txt","w") as f:
    f.write("Satwik Singh is a very talented person.")'''