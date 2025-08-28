'''
def username():
    name = input("Enter your usernname:")
    print("Good day,",name)
username()


def username(name):
    print("Good day,"+ name)
username("Satwik")
username("Satyam")
username("Moham")
username("Rohan")


def username(name, ending):      # Here we use two arguments'name',and 'ending'
    print("Good day,",name,ending)
username("Satwik","Singh")
username("Satyam","Singh")
username("Moham","Kumar")
username("Rohan","Kumar")
'''

def username(name,surname):
    return name+surname
a = username("Satwik"," Singh") 
print(a)
# name = input("Enter your name: ")
# surname = input("Enter your surname: ")
# print(username(name,surname))
