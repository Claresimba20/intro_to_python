import random

def get_computer_choice():
    return random.choice(["rock","paper","scissors"])

def determine_winner(user,computer):
    if user==computer:
        return "draw"
    elif(user=="rock" and computer=="scissors") or\
        (user=="scissors" and computer=="paper") or\
        (user=="paper" and computer=="rock"):
        return "user" 
    else:
        return  "computer"
    
def play_games (rounds=3):
    user_score=0
    computer_score=0
    round_number=1
    win_target=rounds // 2+1

    print(f"Let's play Rock-Paper-Scissors!Best of {rounds} rounds.\n")

    while user_score < win_target and computer_score < win_target and round_number <=rounds:
        print (f"Round {round_number}")
        user_choice = input("Enter rock, paper, or scissors:").lower()

        if  user_choice not in ["rock","paper","scissors"]:
            print("Invalid input.Try again.\n")
            continue

        computer_choice=get_computer_choice()
        print(f"Computer chose:{computer_choice}")

        winner=determine_winner(user_choice,computer_choice)

        if winner=="user":
            user_score +=1
            print("You win this round!\n")
        elif winner=="computer":
            computer_score +=1
            print("Computer wins this round!\n")
        else:
            print("It's a draw\n")

        round_number +=1

    print("Game over!")
    print(f"Final score - You:{user_score}, Computer:{computer_score}")

    if user_score >  computer_score:
            print("You are the overall winner!")
    elif computer_score > user_score:
            print("Computer wins overall!")
    else:
            print("It's a tie!")