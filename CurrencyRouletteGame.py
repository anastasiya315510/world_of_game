#This game will use the free currency api to get the current exchange rate from USD to ILS, will
#generate a new random number between 1-100 a will ask the user what he thinks is the value of
#the generated number from USD to ILS, depending on the user’s difficulty his answer will be
#correct if the guessed value is between the interval surrounding the correct answer


import requests

from Constants import *


def play(difficulty):
    interval = get_money_interval(difficulty)

    user_guess = get_guess_from_user()

    if interval[0] <= user_guess <= interval[1]:
        print("You Won!!!")
        return True
    else:
        print("You Lose!!!")
        return False




def get_guess_from_user():
    return float(input("Please enter your choice:  "))




def get_money_interval(difficulty: int) -> tuple[float, float]:
    """
    Fetch the current USD → ILS exchange rate and calculate
    the acceptable interval based on user difficulty.

    Args:
        difficulty (int): Difficulty level (1–5)

    Returns:
        tuple[float, float]: Lower and upper bounds of the valid interval.
    """

    # 🎮 Ask user for an amount in USD
    try:
        t = float(input("💵 Enter an amount in USD to convert: "))
    except ValueError:
        print("❌ Invalid input! Please enter a number.")


    # 🌍 Fetch exchange rate data
    try:
        response = requests.get(FREE_CURRENCY_API)
        response.raise_for_status()
        data = response.json()
        rate = round(data["data"]["ILS"], ROUND_VALUE)
        print(f"💱 Current USD → ILS rate: {rate}")
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error fetching exchange rate: {e}")

    except KeyError:
        print("⚠️ Error: Unexpected API response format.")


    # 🧮 Calculate correct value and acceptable interval
    correct_value = t * rate
    margin = 5 - difficulty
    low = correct_value - margin
    high = correct_value + margin

    print(f"🎯 Target interval: {round(low, 2)} - {round(high, 2)} ILS")

    return low, high



