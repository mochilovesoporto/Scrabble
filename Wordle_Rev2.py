import random

#Key:
# #correct = same letter, same place
# Misplaced = same letter, wrong place
# Wrong = wrong

#Functions

def intro():
    print("""\nHi! Welcome to Wordle!
    Worlde is a game in which you must guess a word.
    You are given 6 guesses.
    Each time you guess, if the letters in your guess match the letters and order in the Wordle word they will be printed on the screen as "Correct".
    If you guess a correct letter but not in the right order, it will be printed on the screen as "Misplaced".
    If your has letters that are not in the Wordle word at all, then they will be printed on the screen as "Incorrect".
    Let's begin!""")

def word_length():
    global guess_word_length
    guess_word_length = input("\nFirst, decide what is the maximum length of the Wordle word that you wil have to guess. Please enter a number ONLY for this: ")

def get_random_word():
    with open('animals.txt') as animals:
        word_list = [line.lower() for line in animals.readlines() if len(line) <= int(guess_word_length) and all(letter != " " for letter in line)]
    return random.choice(word_list)

def show_guess(word, guess):
    correct_letters = {random_letter for random_letter, correct_letter in zip(word, guess) if random_letter.lower() == correct_letter.lower()}
    misplaced_letters = set(guess) & set(word) - correct_letters
    incorrect_letters = set(guess) - set(word)
    print("Correct letters: ", ",".join(correct_letters))
    print("Misplaced letters: ", ",".join(misplaced_letters))
    print("Incorrect letters: ", ",".join(incorrect_letters))

def game_over():
    print("\n You have lost! Better luck next time. The Wordle word was: " + guess_word)


# Main Function

def main():
    #Pre-process --> Everything needs happen before you main loop runs
    intro()
    word_length()
    guess_word = get_random_word().lower()

    #Process (main loop) --> Code executed during main game loop
    for guess_num in range(1, 7):
        print(guess_word)
        guess = input("\nGuess " + str(guess_num) + ": ")

        show_guess(guess_word, guess)
        if guess.lower() == guess_word.lower():
            print("Woohoo! You got correctly guessed the Worlde word!")
            break

    # Post-process --> Clean-up post main loop
    else:
        game_over()

main()

