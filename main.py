import random
from tkinter.messagebox import YES
game_over = False

while not game_over:
    choices = ["R", "P", "S"]
    computer = random.choice(choices)
    player = input("What's your choice? 'R', 'P' or 'S': ").upper()
    
    if player not in choices:
            print("an error has occur, try again")
            continue
        
    if player == computer:
        print("computer({}):".format(computer),computer)
        print("player({}):".format(player),player)
        print("It's a tie!")

    elif player == "R":
        if computer == "P":
            print("computer({}):".format(computer),computer)
            print("player({}):".format(player),player)
            print("Computer win!")   
            break
        if computer == "S":
            print("computer({}):".format(computer),computer)
            print("player({}):".format(player),player)
            print("You win!")
            break

    elif player == "P":
        if computer == "R":
            print("computer({}):".format(computer),computer)
            print("player({}):".format(player),player)
            print("Computer win!")
            break
        if computer == "S":
            print("computer({}):".format(computer),computer)
            print("player({}):".format(player),player)
            print("You win!")
            break

    elif player == "S":
        if computer == "P":
            print("computer({}):".format(computer),computer)
            print("player({}):".format(player),player)
            print("Computer win!")
            break
        if computer == "R":
            print("computer({}):".format(computer),computer)
            print("player({}):".format(player),player)
            print("You win!")
            break
        
    