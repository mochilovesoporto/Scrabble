import random
from rich.console import Console
from rich.theme import Theme

console = Console(width = 100, theme=Theme({"warning": "red on yellow"}))
console.rule(":leafy_green: Wyrdle :leafy_green:")

#Key:

# #correct = same letter, same place
# Misplaced  same letter, wrong place
# Wrong - wrong

def main():
    #Pre-process --> Everything needs happen before you main loop runs
    intro()
    length = word_length()
    guess_word = get_random_word(length)
    guesses = ["_" * (int(length))] * 6

    #Process (main loop) --> Code executed during main game loop
    for guess_num in range(1, 7):
        print(guess_word)
        guess = input("\nGuess " + str(guess_num) + ": ")
        show_guess(guess_word, guess)
        if guess == guess_word:
            print("\nWoohoo! You got correctly guessed the Worlde word!")
            break

    # Post-process --> Clean-up post main loop
    else:
        game_over(guess_word)

def intro():
    print("""\nHi! Welcome to Wordle!
    Worlde is a game in which you must guess a word.
    You are given 6 guesses.
    Each time you guess, if the letters in your guess match the letters and order in the Wordle word they will be printed on the screen as "Correct".
    If you guess a correct letter but not in the right order, it will be printed on the screen as "Misplaced".
    If your has letters that are not in the Wordle word at all, then they will be printed on the screen as "Incorrect".
    Let's begin!""")

def word_length():
    guess_word_length = input("\nFirst, decide what is the maximum length of the Wordle word that you wil have to guess. Please enter a number ONLY for this: ")
    return guess_word_length

def get_random_word(length):
    with open('animals.txt') as animals:
        word_list = [line.lower().strip() for line in animals.readlines() if (len(line) - 1) == int(length) and all(letter != " " for letter in line)]
    return random.choice(word_list)

def show_guess(word, guess):

    """Show the user's guess on the terminal and classify all letters

    ## Example:
    >>> show_guess("SNAKE", "CRANE")
    Correct letters:  E,A
    Misplaced letters:  N
    Incorrect letters:  C,R"""

    correct_letters = {random_letter for random_letter, correct_letter in zip(word, guess) if random_letter.lower() == correct_letter.lower()}
    misplaced_letters = set(guess) & set(word) - correct_letters
    incorrect_letters = set(guess) - set(word)
    print("\nCorrect letters: ", ",".join(correct_letters))
    print("Misplaced letters: ", ",".join(misplaced_letters))
    print("Incorrect letters: ", ",".join(incorrect_letters))

def refresh_page(headline):
    console.clear() #clear screen
    console.rule("[bold blue]:leafy_green: {} :leafy_green:[/]\n".format(headline)) # print headline on top of screen -- rule = horizontal rule for decoration

def game_over(guess_word):
    print("\nYou have lost! Better luck next time. The Wordle word was: " + guess_word)

if __name__ == "__main__":
    main()

