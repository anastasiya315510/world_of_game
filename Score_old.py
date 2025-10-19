from Utils import SCORES_FILE_NAME


import os


def add_score(difficulty):
    # POINTS_OF_WINNING = (DIFFICULTY X 3) + 5
    difficulty = int(difficulty)
    points_of_winning = difficulty*3 +5


    existing_score = read_file_value()

    existing_score = int(existing_score)

    sum = existing_score + points_of_winning
    write_file_value(sum)



def read_file_value():
    try:
        with open(SCORES_FILE_NAME , "r") as file:
            line = file.readline().strip()
            if line == "":
                return 0
            score = int(line)
            return score
    except FileNotFoundError:
        score = 0
        return score


def write_file_value(score):
    with open(SCORES_FILE_NAME , "w") as file:
        file.write(str(score))


