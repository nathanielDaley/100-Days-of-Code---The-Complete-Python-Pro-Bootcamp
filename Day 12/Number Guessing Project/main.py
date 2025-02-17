import random

from art import logo

EASY = 10
HARD = 5
MAX_RANDOM_NUMBER = 100

def choose_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    while difficulty != 'easy' and difficulty != 'hard':
        difficulty = input("Invalid difficulty chosen.\nChoose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == 'easy':
        return EASY
    else:
        return HARD


print(logo)
print("Welcome to the Number Guess Game!")
print("I'm thinking of a number between 1 and 100.")

randomNumber = random.randint(1, MAX_RANDOM_NUMBER)
attempts = choose_difficulty()
player_guess = 0

while player_guess != randomNumber and attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    player_guess = int(input("Make a guess: "))
    if player_guess < randomNumber:
        print("Too low.")
        attempts -= 1
    elif player_guess > randomNumber:
        print("Too high.")
        attempts -= 1

    if player_guess != randomNumber and attempts > 0:
        print("Guess again.")

if player_guess == randomNumber:
    print(f"You got it! The answer was {randomNumber}.")
else:
    print(f"You lost. The answer was {randomNumber}")