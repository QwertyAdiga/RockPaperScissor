import random
import os
import json

DATA_FILE = os.path.join(os.path.dirname(__file__), "points.json")
try:
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
except Exception as e:
    print(e)

def save(final_winner=None):
    global user_points, com_points, data

    data["user_points_save"] = user_points
    data["com_points_save"] = com_points

    if final_winner == "user":
        data["user_won"] += 1
    elif final_winner == "com":
        data["com_won"] += 1

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def convert():
    global user_choice
    if user_choice == "1":
        user_choice = "rock"
    elif user_choice == "2":
        user_choice = "paper"
    elif user_choice == "3":
        user_choice = "scissor"

real_choice = ["rock", "paper", "scissor"]
user_points = data["user_points_save"]
com_points = data["com_points_save"]

while True:
    com_choice = random.choice(real_choice)
    user_choice = input('''
Enter 1 for Rock
Enter 2 for Paper
Enter 3 for Scissor 
Enter "q" to quit the game :- ''')
    convert()

    if user_choice in real_choice or user_choice == "q" :
        if user_choice == "q":
            print("Your total points is :- ",user_points,"and computer's total points is :-",com_points)
            if user_points > com_points:
                print("Hurray, you are the winner")
                save("user")
            elif com_points > user_points:
                print("Oops, you are the loser")
                save("com")
            elif user_points == 0 and com_points == 0:
                print("You didn't start the game...")
                save()
            else:
                print("Oh!, it's a tie")
                save()
            print(f"Computer won {data["com_won"]} times and you won {data["user_won"]} times in the history")
            break

        if (user_choice == "rock" and com_choice == "scissor") or (user_choice == "paper" and com_choice == "rock") or (user_choice == "scissor" and com_choice == "paper"):
            user_points = user_points + 1
            print(f"Your {user_choice} defeated computer's {com_choice}")
            print(f"Your points is :- {user_points} and computer points is :- {com_points}")
        elif user_choice == com_choice:
            com_points+=1 ; user_points+=1
            print(f"Your computer choose :- {com_choice} and You choose :- {user_choice}")
            print("You and computer put same value")
            print(f"Your points is :- {user_points} and computer points is :- {com_points}\n")

        if (user_choice == "rock" and com_choice == "paper") or (user_choice == "paper" and com_choice == "scissor") or (user_choice == "scissor" and com_choice == "rock"):
            com_points = com_points + 1
            print(f"Computer's {com_choice} beat your {user_choice}") 
            print(f"Your points is :- {user_points} and computer points is :- {com_points}")
    else:
        print("Please enter '1','2','3'")