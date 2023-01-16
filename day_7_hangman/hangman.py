from hangman_words import word
from hangman_art import logo, stages

end_of_game = False
lives = 6

print(logo)

#Create blanks
display = ["-" for _ in range(len(word))]
print(f"Guess the word: {''.join(display)}")

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    # check if a letter already guessed
    if guess in display:
        print(f"You've already guessed {guess}")
    # Check guessed letter
    for position in range(len(word)):
        letter = word[position]
        if letter == guess in word:
            # Replace blank to a letter
            display[position] = letter
    # Check if user is wrong.
    if guess not in word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print("Game over. You lose.")
            print(f"The word was: {word}")
    print(*display, sep="")
    print()
    # Check if user has got all letters.
    if '-' not in display:
        end_of_game = True
        print("You win!")
