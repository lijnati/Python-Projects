import random

def game_choice(user_choice):
    if user_choice == "r":
        user_choice = "rock"
    elif user_choice == "p":
        user_choice = "paper"
    elif user_choice == "s":
        user_choice = "scissors"
    return user_choice

def game_play():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    print("\nWelcome to the Rock Paper Scissors Game!")
    print("\nPlease choose between the following options:")
    print("\n1. Rock - Enter 'r'")
    print("\n2. Paper - Enter 'p'")
    print("\n3. Scissors - Enter 's'")
    print("\n")

    user_choice = input("Enter your choice: ").lower()

    if user_choice not in ['r', 'p', 's']:
        print("\nInvalid choice! Please enter either 'r', 'p', or 's'.")
    else:
        user_choice = game_choice(user_choice)
        print("\nYou chose " + user_choice)
        print("\nThe computer chose " + computer_choice)

        if user_choice == computer_choice:
            print("\nIt's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("\nYou win!")
        else:
            print("\nYou lose!")

if __name__ == "__main__":
    game_play()