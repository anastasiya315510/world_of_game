# This is a simple guess game.
# The game starts by generating a random number between 1 and the value of 'difficulty'.
# The player is then prompted to guess the number.
# The program checks the player's input against the random number and provides feedback.


import random

def generate_number(difficulty):
    random_number =  random.randint(1, difficulty)
    print(f"The number is {random_number}")
    return random_number


def get_guess_from_user(difficulty):
    while True:
        try:
            index = input("Please enter your guess number: ")
            return int(index)
        except ValueError:
            print("Invalid input! Please enter between 1 and " + str(difficulty) + ".")


def compare_results(generated_number, user_guess):
    if generated_number == user_guess:
        print("Correct!")
        return True
    else:
        print("Incorrect!")
        return False


def play(difficulty):
    generated_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    return compare_results(generated_number, user_guess)


