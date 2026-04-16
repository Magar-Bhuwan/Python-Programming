# The game() function in a program lets a user play a game and returns the score as an integer. You need to read a 
# file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update 
# the Hiscore whenever the game() function breaks the Hi-score.

import random

def game():
    score = random.randint(1, 100)
    return score

score = game()

try:
    with open(r"D:\ML with Python\Python\Chapter 9 - File IO\Hi_score.txt", "r") as f:
        hi_score_str = f.read()
        if hi_score_str == "":
            hi_score = 0
        else:
            hi_score = int(hi_score_str)
except FileNotFoundError:
    hi_score = 0

if score > hi_score:
    print(f"Congratulations! You broke the high score. New High Score is {score}!")
    with open(r"D:\ML with Python\Python\Chapter 9 - File IO\Hi_score.txt", "w") as f:
        f.write(str(score))
else:
    print(f"The current high score is {hi_score}. Try again to beat it!")   