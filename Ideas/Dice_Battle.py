on = True
import random

Dice_Types = ["D10", "D20", "D100", "D1000"]


def roll(a, dice_type):
    Roll1 = random.randint(1, a)
    Roll2 = random.randint(1, a)
    print(f"\n\nRolling the {dice_type}...")

    if Roll1 > Roll2:
        print(f"\n\n{Name_1} Rolled a {Roll1} and beats {Name_2}'s roll of {Roll2}!")
    elif Roll1 < Roll2:
        print(f"\n\n{Name_2} Rolled a {Roll2} and beats {Name_1}'s roll of {Roll1}!")
    else:
        print("\n\nIts a tie!")


# ----------------------------------------------------------------------
if __name__ == "__main__":
    while on:
        Name_1 = input("What is your name:  ")
        Name_2 = input("What is your opponents name: ")

        print(f"\n\nHello {Name_1} and {Name_2} And Welcome to Dice battles!!!")
        print("\n\nPICK YOUR DICE TYPE!\n", *Dice_Types, sep="\n")

        Roll = ""
        while Name_1 and Name_2:
            Roll = input("\n\nWhat are you rolling: ")
            if roll not in Dice_Types:
                print("Invalid Dice Type!")

            if Roll == "D10":
                roll(10, "D10")
                Play_again = input("Play again? (y/n): ")
                if Play_again.lower() == "y":
                    on = True
                    continue
                else:
                    print(f"\n\nThanks for playing {Name_1} and {Name_2}!")
                    on = False
                    break

            elif Roll == "D20":
                roll(20, "D20")
                Play_again = input("Play again? (y/n): ")
                if Play_again.lower() == "y":
                    on = True
                    continue
                else:
                    print(f"\n\nThanks for playing {Name_1} and {Name_2}!")
                    on = False
                    break

            elif Roll == "D100":
                roll(100, "D100")
                Play_again = input("Play again? (y/n): ")
                if Play_again.lower() == "y":
                    on = True
                    continue
                else:
                    print(f"\n\nThanks for playing {Name_1} and {Name_2}!")
                    on = False
                    break

            elif Roll == "D1000":
                roll(1000, "D1000")
                Play_again = input("Play again? (y/n): ")
                if Play_again.lower() == "y":
                    on = True
                    continue
                else:
                    print(f"\n\nThanks for playing {Name_1} and {Name_2}!")
                    on = False
                    break
