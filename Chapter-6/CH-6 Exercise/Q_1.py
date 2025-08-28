s1 = int(input("Enter number 1:"))
s2= int(input("Enter number 1:"))
s3= int(input("Enter number 1:"))
s4= int(input("Enter number 1:"))

if(s1>s2 and s1>s3 and s1>s4):
    print("The greatest number is:",s1)
elif(s2>s1 and s2>s3 and s2>s4):
    print("The greatest number is:",s2)
elif(s3>s1 and s3>s2 and s3>s4):
    print("The greatest number is:",s3)
else:
    print("The greatest number is:",s4)