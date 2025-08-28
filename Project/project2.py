# Snkae , Water , Gun game
# Snake Water Gun Game in Python
# Snake vs Water -> Snake drinks the water hence wins.
# Water vs Gun -> The gun will drown in water, hence a point for water
# Gun vs Snake -> Gun will kill the snake and win
# Author: Satwik Singh
# Date: 17/06/2025
import random
'''
1 for snake
2 for water
3 for gun
'''
computer = random.choice([1,2,3])
your_choice = input("Enter your choice:")
dict = {"s":1,"w":2,"g":3}
reversedict = {1:"snake",2:"water",3:"gun"}
you = dict[your_choice]
print(f"your choice is {reversedict[you]}\ncomputer choice is {reversedict[computer]}")
'''
if you == computer:
    print("Tie")
elif you == 1 and computer == 2: #1-2=-1
    print("You win")
elif you == 2 and computer == 3:#2-3=-1
    print("You win")
elif you == 3 and computer == 1:#3-1=2
    print("You win")
elif you == 1 and computer == 3:#1-3=-2
    print("You loose")
elif you == 3 and computer == 2:#3-2=1
    print("You loose")
elif you ==2 and computer == 1:#2-1=1
    print("You loose")
else:
    print("Invalid input")
    '''
# short cut for above code
if (you-computer) == -1 or(you-computer)==2:
    print("You win")
elif (you-computer)==0:
    print("Tie")

elif (you-computer)==1 or(you-computer)==-2:
    print("You loose")
else:
    print("Invalid input")
