Rock-Paper-Scissors Game
Overview

This repository contains a simple command-line implementation of the classic Rock-Paper-Scissors game in Python. The user competes against the computer, which selects its moves randomly. The game continues until either the user or the computer achieves three victories.

The project is designed to demonstrate basic control flow, conditionals, and input handling in Python.

Features

Interactive gameplay between user and computer.

Randomized computer moves using Python's random module.

Score tracking for both user and computer.

Automatic game termination once a player reaches three wins.

Clear round-by-round feedback.

Game Rules

The rules are consistent with the traditional Rock-Paper-Scissors game:

User Choice	Computer Choice	Winner	Explanation
Rock	Scissor	User	Rock beats Scissor
Paper	Rock	User	Paper wraps Rock
Scissor	Paper	User	Scissor cuts Paper
Rock	Paper	Computer	Paper wraps Rock
Paper	Scissor	Computer	Scissor cuts Paper
Scissor	Rock	Computer	Rock beats Scissor
Same Choice	Same Choice	Tie	Both players selected same

The first player to reach three points wins the match.

Code Implementation
import random

items = ["Rock", "Paper", "Scissor"]

comp_var = 0
user_var = 0

while comp_var <= 3 or user_var <= 3:
    user_choice = input("Enter your move = Rock, Paper or Scissor: ")
    comp_choice = random.choice(items)
    print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

    if user_choice.lower() == "rock" and comp_choice == "Paper":
        print("Paper wraps rock. Thus, computer wins")
        comp_var += 1
    elif user_choice.lower() == "rock" and comp_choice == "Scissor":
        print("Rock beats scissor. Thus, user wins")
        user_var += 1
    elif user_choice.lower() == "paper" and comp_choice == "Rock":
        print("Paper wraps rock. Thus, user wins")
        user_var += 1
    elif user_choice.lower() == "paper" and comp_choice == "Scissor":
        print("Scissor cuts paper. Thus, computer wins")
        comp_var += 1
    elif user_choice.lower() == "scissor" and comp_choice == "Paper":
        print("Scissor cuts paper. Thus, user wins")
        user_var += 1
    elif user_choice.lower() == "scissor" and comp_choice == "Rock":
        print("Rock beats scissor. Thus, computer wins")
        comp_var += 1
    else:
        print("Tie between computer and user.")

    print(f"Total score — Computer: {comp_var}, User: {user_var}")

    if user_var == 3:
        print("User wins the game!")
        break
    if comp_var == 3:
        print("Computer wins the game!")
        break

print("Game is complete. Thank you for playing!")

Execution Instructions

Ensure that Python 3.6 or higher is installed on your system.

Save the program in a file named rock_paper_scissor.py.

Open a terminal or command prompt in the same directory as the file.

Execute the following command:

python rock_paper_scissor.py


Follow the on-screen instructions to play.

Example Output
Enter your move = Rock, Paper or Scissor: rock
User choice = rock, Computer choice = Scissor
Rock beats scissor. Thus, user wins
Total score — Computer: 0, User: 1
...
User wins the game!
Game is complete. Thank you for playing!

Possible Extensions

Add input validation for incorrect spellings or invalid entries.

Allow users to set a custom winning score.

Introduce a graphical user interface (GUI) using Tkinter or Pygame.

Maintain a persistent score history across multiple sessions.

Extend the game with additional choices such as Lizard and Spock.

Dependencies

Python Standard Library (random module only).

No external packages are required.

License

This project is released under the MIT License.
You are free to use, modify, and distribute this code for educational or research purposes.

Citation

If you use or modify this project in academic work or teaching materials, please cite it as:

Rock-Paper-Scissors Python Implementation.
Version 1.0, 2025.
Available on GitHub.
