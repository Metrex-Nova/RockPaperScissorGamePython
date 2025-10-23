Rock-Paper-Scissors Game
========================

Overview
--------
This project implements a simple command-line version of the Rock-Paper-Scissors game using Python. 
The user plays against the computer, which randomly selects its move. 
The game continues until either the user or the computer wins three rounds.

This program demonstrates the use of loops, conditional logic, user input, and random number generation in Python.

Features
--------
- Interactive user input and computer-generated responses
- Score tracking for both user and computer
- Automatic termination when either side reaches three wins
- Clear textual feedback for every round

Rules
-----
The rules of Rock-Paper-Scissors are as follows:

User Choice | Computer Choice | Winner   | Explanation
-------------|----------------|-----------|-----------------------------
Rock         | Scissor        | User      | Rock beats Scissor
Paper        | Rock           | User      | Paper wraps Rock
Scissor      | Paper          | User      | Scissor cuts Paper
Rock         | Paper          | Computer  | Paper wraps Rock
Paper        | Scissor        | Computer  | Scissor cuts Paper
Scissor      | Rock           | Computer  | Rock beats Scissor
Same Choice  | Same Choice    | Tie       | Both selected same option

The first to reach three points wins the game.

Source Code
-----------
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

How to Run
----------
1. Ensure Python 3.6 or higher is installed on your computer.
2. Save the code in a file named 'rock_paper_scissor.py'.
3. Open a terminal or command prompt in the file’s directory.
4. Run the following command:
   python rock_paper_scissor.py
5. Follow the on-screen instructions to play the game.

Sample Output
-------------
Enter your move = Rock, Paper or Scissor: rock
User choice = rock, Computer choice = Scissor
Rock beats scissor. Thus, user wins
Total score — Computer: 0, User: 1
...
User wins the game!
Game is complete. Thank you for playing!

Future Enhancements
-------------------
- Input validation for invalid entries
- Configurable winning score limit
- Graphical User Interface (GUI) using Tkinter or Pygame
- Score persistence between sessions
- Extended game versions such as Rock-Paper-Scissors-Lizard-Spock

Requirements
------------
- Python 3.6 or later
- No external dependencies (uses Python standard library only)

License
-------
This project is licensed under the MIT License.
You may freely use, modify, and distribute this program for educational or research purposes.

Author
------
Developed as an introductory Python project demonstrating basic programming constructs and logical control flow.
