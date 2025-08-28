name = input("Enter your name: ")

if name.isdigit():
    print("Please enter a valid name.")
    exit()

marks = int(input("Enter your marks: "))
number = int(input("Enter the mobile number: "))

a = "The name of the student is {}, his marks are {} and phone number is {}".format(name, marks, number)
print(a)
