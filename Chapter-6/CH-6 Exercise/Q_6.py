Marks = int(input('Enter your marks:'))

if(90<=Marks<=100):
    print("You are in grade \'EX\'")
if(80<=Marks<90):
    print("You are in grade \'A\'")
if(70<=Marks<80):
    print("You are in grade \'B\'")
if(60<=Marks<70):
    print("You are in grade \'C\'")
if(50<=Marks<60):
    print("You are in grade \'D\'")
if(0<Marks<50):
    print("You are in grade\'E\'")
elif(Marks<=0):
    print("You are entring invalid marks.")
else:
    print("You are entring invalid marks.")