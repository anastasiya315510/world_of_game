from games.GuessGame import play as guess
from games.MemoryGame import play as memory
from games.CurrencyRouletteGame import play as currency_roulette

def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG).")
    print("Here you can find many cool games to play.\n")


def load_game():
    print("Please choose a game number to play:\n")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n")


    while True:
        try:
            number = int(input("Your number: "))
            if 1<=number<=3:
                print(f"{number} is a valid number.".format(number=number))
                break
            else:
                print("Please enter a number from 1 till 3")
        except ValueError:
            print("Please enter a number from 1 till 3")



    while True:
        try:
            difficulty = int(input("Please choose game difficulty from 1 to 5: "))
            if 1<=difficulty<=5:
                break
            else:
                print("Please enter a number from 1 till 5")
        except ValueError:
            print("Please enter a number from 1 till 5")

    match number:
        case 1:
            print("Memory Game\n")
            memory(difficulty)
        case 2:
            print("Guess Game starts!!!!\n")
            guess(difficulty)
        case 3:
            print("You selected option 3!\n")
            currency_roulette(difficulty)
        case _:
            print("Invalid input! Please enter 1, 2, or 3.")


