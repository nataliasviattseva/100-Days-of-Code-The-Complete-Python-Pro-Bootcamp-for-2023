from random import randint
from art import logo


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def make_guess():
    done = False
    while not done:
        user_number = input("Make a guess: ")
        if not user_number.isdigit():
            print("Enter a valid number")
            continue
        elif int(user_number) < 0 or int(user_number) > 100:
            print("Enter number between 0 and 100")
        else:
            done = True
    return int(user_number)


def check_answer(answer, attempts):
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number")
        user_number = make_guess()
        if answer < user_number:
            print("Too high.")
        elif answer > user_number:
            print("Too low.")
        else:
            print(f"You got it! The answer was {answer}.")
            break
        print("Guess again.")
        attempts -= 1
    if attempts == 0:
        print("You've run out of guesses, you lose.")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "hard":
        return HARD_LEVEL_TURNS
    else:
        return EASY_LEVEL_TURNS


def welcome():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("# I'm thinking of a number between 1 and 100.")


def set_answer():
    return randint(1, 100)


welcome()
check_answer(set_answer(), set_difficulty())
