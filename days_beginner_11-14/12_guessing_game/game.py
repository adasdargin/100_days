# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from logo import logo

answer = random.randint(1, 100)
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty_level == 'easy':
    attempts = 10
else:
    attempts = 5

correct_guess = False
while not correct_guess:
    if attempts != 0:
        print(f"You have {attempts} attempts remaining to guess the number")
        user_guess = int(input("Make a guess: "))
        if user_guess > answer:
            attempts -= 1
            print("Too high")
        elif user_guess < answer:
            attempts -= 1
            print("Too low.")
        elif user_guess == answer:
            print(f"You got it! The answer was {answer}.")
            correct_guess = True
    else:
        print("You've run out of guesses, you lose.")
        correct_guess = True