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
        print("computer:",computer)
        print("player:",player)
        print("It's a tie!")

    elif player == "R":
        if computer == "P":
            print("computer:",computer)
            print("player:",player)
            print("You lose!")    
        if computer == "S":
            print("computer:",computer)
            print("player:",player)
            print("You win!")

    elif player == "P":
        if computer == "R":
            print("computer:",computer)
            print("player:",player)
            print("You lose!")
               
        if computer == "S":
            print("computer:",computer)
            print("player:",player)
            print("You win!")

    elif player == "S":
        if computer == "P":
            print("computer:",computer)
            print("player:",player)
            print("You lose!")
        if computer == "R":
            print("computer:",computer)
            print("player:",player)
            print("You win!")

    