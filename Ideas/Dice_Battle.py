on = True
import random

Dice_Types = ["D10", "D20", "D100", "D1000"]


def roll(a, dice_type):
    Roll1 = random.randint(1, a)
    Roll2 = random.randint(1, a)
    print(f"Rolling the {dice_type}...")

    if Roll1 > Roll2:
        print(f"{Name_1} Rolled a {Roll1} and beats {Name_2}'s roll of {Roll2}!")
    elif Roll1 < Roll2:
        print(f"{Name_2} Rolled a {Roll2} and beats {Name_1}'s roll of {Roll1}!")
    else:
        print("Its a tie!")


# ----------------------------------------------------------------------
if __name__ == "__main__":
    while on:
        Name_1 = input("What is your name:  ")
        Name_2 = input("What is your opponents name: ")

        print(f"Hello {Name_1} and {Name_2} And Welcome to Dice battles!!!")
        print("PICK YOUR DICE TYPE!\n", *Dice_Types, sep="\n")

        Roll = input("What are you rolling: ")

        if Roll == "D10":
            roll(10, "D10")

            Play_again = input("Play again? (y/n): ")
            on = Play_again.lower() == "y"

        if Roll == "D20":
            roll(20, "D20")
            Play_again = input("Play again? (y/n): ")
            on = Play_again.lower() == "y"

        if Roll == "D100":
            roll(100, "D100")
            Play_again = input("Play again? (y/n): ")
            on = Play_again.lower() == "y"

        if Roll == "D1000":
            roll(1000, "D1000")
            Play_again = input("Play again? (y/n): ")
            on = Play_again.lower() == "y"
