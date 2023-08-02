import random


def roll():
    min_val = 1
    max_val = 6
    roll = random.randint(min_val, max_val)

    return roll


while True:
    players = input("Enter the number of players (1-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must Be Between 2 and 4 players")
    else:
        print("Invalid, Try Again")

max_score = 50
