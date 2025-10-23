import random

items = ["Rock", "Paper", "Scissor"]

permission = True
comp_var = 0
user_var = 0
while(comp_var <= 3 or user_var <= 3) : 
    user_choice = input("Enter your move = Rock, Paper or Scissor: ")
    comp_choice = random.choice(items)
    print(f"User choice = {user_choice}, Computer choice = {comp_choice}")
    if(user_choice.lower() == "rock" and comp_choice == "Rock"):
        print("Tie between computer and user.")
        print(f"total score of computer: {comp_var}, total score of user: {user_var}")
    elif(user_choice.lower() == "rock" and comp_choice == "Paper"):
        print("Paper wraps rock. Thus, computer wins")
        comp_var = comp_var + 1
        print(f"total score of computer: {comp_var}, total score of user: {user_var}")
    elif(user_choice.lower() == "rock" and comp_choice == "Scissor"):
        print("Rock beats scissor. Thus, user wins")
        user_var = user_var + 1
        print(f"total score of computer: {comp_var}, total score of user: {user_var}")
    elif(user_choice.lower() == "paper" and comp_choice == "Paper"):
        print("Tie between computer and user.")
        print(f"total score of computer: {comp_var}, total score of user: {user_var}")
    elif(user_choice.lower() == "paper" and comp_choice == "Rock"):
        print("Paper wraps rock. Thus, user wins")
        user_var = user_var + 1
        print(f"total score of computer: {comp_var}, total score of user: {user_var}")
    elif(user_choice.lower() == "paper" and comp_choice == "Scissor"):
        print("Scissor cuts paper. Thus, computer wins")
        comp_var = comp_var + 1
        print(f"total score of computer: {comp_var}, total score of user: {user_var}")
    elif(user_choice.lower() == "scissor" and comp_choice == "Scissor"):
        print("Tie between computer and user.")
        print(f"total score of computer: {comp_var}, total score of user: {user_var}")
    elif(user_choice.lower() == "scissor" and comp_choice == "Paper"):
        print("Scissor cuts paper. Thus, user wins")
        user_var = user_var + 1
        print(f"total score of computer: {comp_var}, total score of user: {user_var}")
    elif(user_choice.lower() == "scissor" and comp_choice == "Rock"):
        print("Rock beats scissor. Thus, computer wins")
        comp_var = comp_var + 1
        print(f"total score of computer: {comp_var}, total score of user: {user_var}")
    if(user_var == 3):
        print("user wins.")
        break
    if(comp_var == 3):
        print("computer wins.")
        break
print("Game is complete. Thankyou for playing.")





