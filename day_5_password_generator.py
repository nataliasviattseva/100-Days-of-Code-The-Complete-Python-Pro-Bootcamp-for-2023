# https://replit.com/@nsviattseva/password-generator-start#main.py

import random
import string

print("Welcome to the PyPassword Generator!")
list = []
nr_letters = input("How many letters would you like in your password?")
nr_symbols = input("How many symbols would you like?")
nr_numbers = input("How many numbers would you like?")

for _ in range(0, int(nr_letters)):
    list.append(random.choice(string.ascii_letters))

for _ in range(0, int(nr_symbols)):
    list.append(random.choice(string.punctuation))

for _ in range(0, int(nr_numbers)):
    list.append(random.choice(string.digits))

random.shuffle(list)

print("Your password is: " + ''.join(list))

