# a = (int(input("Enter a number:")))
# b = (int(input("Enter a number:")))
# c = (int(input("enter a number:")))

# avg = a+b+c/3
# print(avg)
# a = (int(input("Enter a number:")))
# b = (int(input("Enter a number:")))
# c = (int(input("enter a number:")))

# avg = a+b+c/3
# print(avg)

# we have the above program too many time so we use finction for it.

# By using function we can reduce the number of lines of code.

def avg():                                # we can use any name for the function
    a = (int(input("Enter a number:")))   # These lines are called defination.
    b = (int(input("Enter a number:")))
    c = (int(input("enter a number:")))
    avg = (a+b+c)/3
    print(avg)
avg()                                      # These lines are called calling the function, mean Call.
avg()