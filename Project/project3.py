import random
n = random.randint(1,100)
a = 0
guess  = 1
while a != n:
    a = int(input("Enter the number:"))
    if (a>n):
        print("Too high")
    elif (a<n):
        print("Too low")
    else:
        print("Congratulations you won")
        break
    guess+=1
print("You took",guess,"guesses")