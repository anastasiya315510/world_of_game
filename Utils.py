import os

import platform
import time

SCORES_FILE_NAME = "./Scores.txt"

BAD_RETURN_CODE = -1


def screen_cleaner():
    system = platform.system()
    if system == "Windows":
        os.system("cls")
    else:
        os.system("clear")

