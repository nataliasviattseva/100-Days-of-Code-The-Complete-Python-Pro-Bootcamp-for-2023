# https://replit.com/@nsviattseva/rock-paper-scissors-start#main.py

# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

rps = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

if user_choice not in (0, 1, 2):
    print("You typed an invalid number.")
else:
    print(rps[user_choice])
    print(f"Computer chose:\n {rps[computer_choice]}")

    if user_choice == computer_choice:
        print("Draw!")
    elif (computer_choice == 0 and user_choice == 2) or (computer_choice > user_choice):
        print("You lose!")
    elif (user_choice == 0 and computer_choice == 2) or (computer_choice > user_choice):
        print("You win!")
