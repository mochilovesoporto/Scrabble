import random

print("""\nHi! Welcome to Wordle!
    Worlde is a game in which you must guess a word.
    You are given 6 guesses.
    Each time you guess, if the letters in your guess match the letters and order in the Wordle word they will be printed on the screen as "Correct".
    If you guess a correct letter but not in the right order, it will be printed on the screen as "Misplaced".
    If your has letters that are not in the Wordle word at all, then they will be printed on the screen as "Incorrect".
    Let's begin!""")

guess_word_length = input("\nFirst, decide what is the maximum length of the Wordle word that you wil have to guess. Please enter a number ONLY for this: ")

with open('animals.txt') as animals:
    word_list = [line.lower().strip() for line in animals.readlines() if
                 len(line) <= int(guess_word_length) and all(letter != " " for letter in line)]

print(word_list)
guess_word = random.choice(word_list)

for guess_num in range(1, 7):
    print(guess_word)
    guess = input("\nGuess " + str(guess_num) + ": ")

    if guess == guess_word:
        print("Woohoo! You got correctly guessed the Worlde word!")
        break

else:
    print("\n You have lost! Better luck next time. The Wordle word was: " + guess_word)