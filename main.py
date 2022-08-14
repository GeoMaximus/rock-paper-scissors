import random
from enum import IntEnum

class Choice(IntEnum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

def getUserChoice():
    choices = [f"{choice.name}[{choice.value}]" for choice in Choice]
    choices_str = ", ".join(choices)
    choice = int(input(f"Enter a choice ({choices_str}): "))
    action = Choice(choice)
    return action

def getComputerChoice():
    choice = random.randint(0, len(Choice) - 1)
    action = Choice(choice)
    return action

def getWinner(user, computer):
    if(user == computer):
        print("It's a tie!")
    elif(user == Choice.ROCK and computer == Choice.SCISSORS):
        print("You win!")
    elif(user == Choice.ROCK and computer == Choice.PAPER):
        print("You lose!")
    elif(user == Choice.PAPER and computer == Choice.ROCK):
        print("You win!")
    elif(user == Choice.PAPER and computer == Choice.SCISSORS):
        print("You lose!")
    elif(user == Choice.SCISSORS and computer == Choice.ROCK):
        print("You lose!")
    elif(user == Choice.SCISSORS and computer == Choice.PAPER):
        print("You win!")

while True:
    try:
        userChoice = getUserChoice()
    except ValueError:
        print("Invalid choice!")
        continue

    computerChoice = getComputerChoice()
    print("Computer choice:", computerChoice.name + " Your choice:", userChoice.name)
    getWinner(userChoice, computerChoice)

    again = input("Play again? (y/n): ")
    if(again == "n"):
        break