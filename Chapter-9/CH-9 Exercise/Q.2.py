import random
def game():
    print("You are playing a game.")
    score = random.randint(0,100)
    with open("highscore.txt") as f:
        highscore = f.read()
        if highscore!="":
            highscore = int(highscore)
        else:
            highscore = 0
    print(f"Your score is {score}")
    if score>highscore:
        print("You have just broken the high score!")
        with open("highscore.txt","w") as f:
            f.write(str(score))
    else:
        print("You didn't break the high score.")
    print("Do you want to play again?")
    play_again = input("Enter 'y' for yes and 'n' for no: ")
    if play_again == 'y':
        game()
    else:
        print("Thank you for playing!")
        exit()
    return score
game()        