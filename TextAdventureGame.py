''' 
https://github.com/lijnati/Python-Projects

'''
# Start the game
def start_game():
    print("Welcome to the Adventure Game!")
    print("You can type 'start' to begin your adventure, or 'quit' to exit the game.")

# Print out the intro
def print_intro():
    print("")
    print("You are a lost traveler in a dark forest. You must find your way out.")
    print("There are paths to your left and right, but you don't know which one to take.")
    print("")

# First path option
def first_path():
    print("You took the first path and encountered a fierce bear!")
    print("The bear sees you and charges towards you! What do you do?")
    print("1. Try to fight the bear off with your fists.")
    print("2. Run in the opposite direction as the bear.")

    user_choice = input("Enter the number of your choice: ")

    if user_choice == "1":
        print("You try to fight the bear, but it is too strong and easily defeats you.")
        print("The bear then eats you, and you die a painful death.")
        game_over()
    elif user_choice == "2":
        print("You manage to run in time and get away from the bear.")
        print("However, you find yourself deeper in the forest.")
        second_path()
    else:
        print("Invalid choice. Please try again.")
        first_path()

# Second path option
def second_path():
    print("You took the second path and come across a raging river.")
    print("There is no bridge, and you see no other way across the river.")
    print("1. Try to swim across the river.")
    print("2. Look for another path to the right.")

    user_choice = input("Enter the number of your choice: ")

    if user_choice == "1":
        print("You attempt to swim across the river, but the current is too strong.")
        print("You are swept away and drown in the river.")
        game_over()
    elif user_choice == "2":
        print("You walk down the path to the right, hoping it leads you out of the forest.")
        third_path()
    else:
        print("Invalid choice. Please try again.")
        second_path()

# Third path option
def third_path():
    print("You come across a dense thicket that blocks your path.")
    print("You must either push your way through the thicket or turn back.")
    print("1. Try to push your way through the thicket.")
    print("2. Turn back and choose a different path.")

    user_choice = input("Enter the number of your choice: ")

    if user_choice == "1":
        print("You attempt to push your way through the thicket, but it is too dense.")
        print("You get stuck and are unable to move any further.")
        game_over()
    elif user_choice == "2":
        print("You turn back and choose the path to the left.")
        print("You finally find your way out of the forest and into a beautiful meadow.")
        print("You are free!")
        game_over()
    else:
        print("Invalid choice. Please try again.")
        third_path()

# Game over
def game_over():
    print("Game Over.")
    exit()

# Main game loop
def main():
    start_game()

    while True:
        user_input = input("> ")

        if user_input == "quit":
            game_over()
        elif user_input == "start":
            print_intro()
            print("")
            print("Which path do you choose?")
            print("1. The first path.")
            print("2. The second path.")

            user_choice = input("Enter the number of your choice: ")

            if user_choice == "1":
                first_path()
            elif user_choice == "2":
                second_path()
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Invalid command. Please try again.")

# Run the game
if __name__ == "__main__":
    main()