'''
We are going to write a program that generates a random numbers and asks the user to gues it.

If the player's guess is higher than the actual number, the program displays "Lower number please". 
Similarly, if the user guess is too low, the program prints "Higher number please" 
When user gues the correct number, the program displays the number of guess the player use to arrive at the
number.

'''

# import random

# n = random.randint(1, 100)

# guesses = 0
# a = -1            # Initialize a with a value that is not equal to n

# while(a != n):
#     guesses += 1

#     a = int(input("Enter the guess number between 1 to 100 number: "))
#     if (a > n):
#         print("Higher number you have entered. please enter lower number than you entered number. ")
    
#     elif (a < n):
#         print("Lower number you have entered. please entered hihger number than you entered number. ")

# print(f"You have guessed the correct number in {guesses} attempt. ")


import random

n = random.randint(1, 50)
a = -1
count = 0
while(a != n):
    count += 1
    a = int(input("Enter your guess number between (1 - 50) number: "))

    if (a > n):
        print("High number you have entered. Please entered lower number. ")

    elif (a < n):
        print("Low number you have entered. Please entered higher number. ")

print(f"Congratualtion! You have guessed the correct number {n} in {count} attempt. ")