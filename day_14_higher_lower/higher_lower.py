from art import logo, vs
from game_data import data
from random import randint


def select_random_entry():

    random = randint(0, len(data) - 1)
    return [data[random].get("name"), data[random].get("follower_count"), \
           data[random].get("description"), data[random].get("country")]


def compare(a, b, score):
    # print(f"followers a: {a}, followers b: {b}")
    end_game = False

    while not end_game:

        choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        if a == max(a, b) and choice == "a":
            score += 1
            print(f"You're right! Current score: {score}.")
            compare(a, select_random_entry()[1], score)
        elif b == max(a, b) and choice == "b":
            score += 1
            print(f"You're right! Current score: {score}.")
            compare(b, select_random_entry()[1], score)
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            end_game = True


def game_round():

        print(logo)
        name_a = select_random_entry()[0]
        follower_count_a = select_random_entry()[1]
        description_a = select_random_entry()[2]
        country_a = select_random_entry()[3]
        print(f'Compare A: {name_a}, a {description_a}, from {country_a}')
        print(vs)
        name_b = select_random_entry()[0]
        follower_count_b = select_random_entry()[1]
        description_b = select_random_entry()[2]
        country_b = select_random_entry()[3]
        print(f'Compare B: {name_b}, a {description_b}, from {country_b}\n')
        score=0
        compare(follower_count_a, follower_count_b, score)


game_round()

