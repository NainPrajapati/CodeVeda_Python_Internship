# Level 1 - Task 2
# Number Guessing Game
# Codveda Python Internship

import random


def number_guessing_game():
    print("===== Number Guessing Game =====")
    print("I have selected a number between 1 and 100.")
    print("You have 7 attempts to guess it correctly.\n")

    secret_number = random.randint(1, 100)
    max_attempts = 7
    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))

            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too Low! Try again.\n")
            elif guess > secret_number:
                print("Too High! Try again.\n")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
                return

        except ValueError:
            print("Invalid input! Please enter a valid number.\n")

    print(f"❌ Game Over! The correct number was {secret_number}.")

number_guessing_game()
