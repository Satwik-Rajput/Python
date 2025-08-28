s = int(input("Enter your age number:"))

# First if statement.
if(s>=18):
    print("You are in prime age.")
    print("Congratulation")

elif(s<0):
    print("You are entering invalid age.")

elif(s==0):
    print("You are putting invalid age.")

else:
    print("you are in age of preparing yourself for your prime.")

# second if statement.
if(s%2==0):
    print("Your age is even.")
else:
    print("Your age is odd.")