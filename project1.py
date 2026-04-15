#Rock, Paper and Scissor game

'''
1 for Rock
2 for Paper
3 for Scissor
'''
# import random
# computer = random.choice([1,2,3])
# you = input("Enter your choice: (r = Rock, p = Paper and s = Scissor): ")
# youDict = {"r": 1, "p": 2, "s": 3}
# revDict = {1:"Rock", 2:"Paper", 3:"Scissor"}

# user = youDict[you]
# print(f"You choose : {revDict[user]}\nComputer chose : {revDict[computer]}")

# if(computer == user):
#     print("Draw.")

# else:
#     if(computer == 1 and user == 2):
#         print("You Won!")
#     elif(computer == 1 and user == 3):
#         print("Computer Won!")
#     elif(computer == 2 and user == 1):
#         print("Computer Won!")
#     elif(computer == 2 and user == 3):
#         print("You Won!")
#     elif(computer == 3 and user == 1):
#         print("You Won!")
#     elif(computer == 3 and user == 2):
#         print("Computer Won!")
#     else:
#         print("Invalid Entry! ")

import tkinter as tk
import random

# Choices
choices = {"r": "Rock", "p": "Paper", "s": "Scissors"}

# Game logic
def play(user_choice):
    computer_choice = random.choice(list(choices.keys()))

    user_text.set(f"You chose: {choices[user_choice]}")
    comp_text.set(f"Computer chose: {choices[computer_choice]}")

    if user_choice == computer_choice:
        result_text.set("🤝 It's a Draw!")
    elif (
        (user_choice == "r" and computer_choice == "s") or
        (user_choice == "p" and computer_choice == "r") or
        (user_choice == "s" and computer_choice == "p")
    ):
        result_text.set("🎉 You Win!")
    else:
        result_text.set("💻 Computer Wins!")

# Create window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")

# Text variables
user_text = tk.StringVar()
comp_text = tk.StringVar()
result_text = tk.StringVar()

# Title
tk.Label(root, text="Rock Paper Scissors Game", font=("Arial", 16)).pack(pady=10)

# Buttons
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="Rock 🪨", width=10, command=lambda: play("r")).grid(row=0, column=0, padx=5)
tk.Button(frame, text="Paper 📄", width=10, command=lambda: play("p")).grid(row=0, column=1, padx=5)
tk.Button(frame, text="Scissors ✂️", width=10, command=lambda: play("s")).grid(row=0, column=2, padx=5)

# Output labels
tk.Label(root, textvariable=user_text, font=("Arial", 12)).pack(pady=5)
tk.Label(root, textvariable=comp_text, font=("Arial", 12)).pack(pady=5)
tk.Label(root, textvariable=result_text, font=("Arial", 14, "bold")).pack(pady=10)

# Run app
root.mainloop()