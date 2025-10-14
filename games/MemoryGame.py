#The purpose of memory game is to display an amount of random numbers to the users for 0.7
#seconds and then prompt them from the user for the numbers that he remember. If he was right
#with all the numbers the user will win otherwise he will lose.
import random
from typing import List


def is_list_equal(list_from_user, list):
    if list_from_user == list:
        print("You Won!")
        return True
    else:
        print("You Lose!")
        return False


def generate_sequence(difficulty):
    list: List[int] = []
    for i in range(difficulty):
        random_number = random.randint(1, 101)
        list.append(random_number)
        
    print(list)
    return list


def get_list_from_user(difficulty):
    list: List[int] = []

    for i in range(difficulty):
        while True:
            try:
                user_input_value = int(input("Your number from 1 to 101: ") )
                if 1<= user_input_value  <=101   :
                    list.append(user_input_value)
                    break
                else:
                    print("Invalid input. Please, enter number from 1 to 101")
            except ValueError:
                print("Invalid input type. Please, enter number from 1 to 101")

    return list








def play(difficulty):
    list: List[int] = generate_sequence(difficulty)
    list_from_user = get_list_from_user(difficulty)
    is_list_equal(list_from_user, list)