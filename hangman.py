'''
https://github.com/lijnati/Python-Projects

'''

import random

# Welcome the user and explain the rules
print("Welcome to Hangman!")
print("I'm thinking of a word that is between 3 and 10 letters long.")

# Set up the word bank and choose a random word
word_bank = "ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra".split()
word = random.choice(word_bank)

# Set up variables to keep track of the game state
guessed_letters = []
attempts_left = 10

# Loop until the word is guessed or the player runs out of attempts
while attempts_left > 0 and "_" in word:
    # Display the current game state
    print("\nAttempts left: " + str(attempts_left))
    print("Guessed letters: " + " ".join(guessed_letters))
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print(display.strip())

    # Get a guess from the player
    guess = input("\nEnter your guess: ").lower()

    # Check if the guess is a letter
    if len(guess) == 1 and guess.isalpha():
        if guess not in guessed_letters:
            guessed_letters.append(guess)
            if guess not in word:
                attempts_left -= 1
    elif len(guess) == 0:
        print("Please enter a letter.")
    else:
        print("Invalid input. Please enter a single letter.")

# Display the final game state
if "_" in word:
    print("\nYou ran out of attempts! The word was " + word + ".")
else:
    print("\nCongratulations! You guessed the word: " + word + ".")

# Ask the player if they want to play again
play_again = input("\nDo you want to play again? (yes or no) ").lower()
if play_again.startswith("y"):
    print("\nGreat! Starting a new game...")
    # Reset the game state
    guessed_letters = []
    attempts_left = 10
else:
    print("\nThanks for playing! Goodbye.")