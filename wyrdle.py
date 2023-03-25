import random
from rich.console import Console
from rich.theme import Theme
from string import ascii_letters, ascii_uppercase
import enchant

def main():
    #Pre-process --> Everything needs happen before you main loop runs
    global console
    console = Console(width=120, theme=Theme({"warning": "red on yellow"}))
    refresh_page("Wyrdle")

    intro()
    length = word_length()
    word = get_random_word(length)
    num_guesses = 6
    guesses = ["_" * (int(length))] * num_guesses

    #Process (main loop) --> Code executed during main game loop
    for idx in range(6):
        print(word)
        refresh_page("Guess {}".format(idx + 1))
        show_guesses(guesses, word)
        guesses[idx] = input("\nGuess word: ")

        d = enchant.Dict("en_Au")
        while d.check(guesses[idx]) == False:
            guesses[idx] = input("\nYou have not entered an english word, please try again: ")
        print("Hint - The word starts with: " + (word[0]).upper())

        if guesses[idx] == word:
            break

    # Post-process --> Clean-up post main loop
    game_over(guesses, word, correctly_guessed= guesses[idx] == word)

def intro():
    console.print("""\nHi! Welcome to Wyrdle!
    
    Wyrlde is a game in which you must guess a secret randomly generated word.
    This word could be a type of animal, reptile, insect or fish.
    You are given a total of 6 guesses to guess the secret word.
    Pretty tricky right!?
    
    Each guess will be shown on the screen with each letter highlighted in a color:
        [bold white on green]Green[/] = Correct letters in the correct order.
        [bold white on yellow]Yellow[/] = Correct letters in the wrong order.
        [white on #666666]Grey[/] = Wrong letters. 
    
    Let's begin!""")


def word_length():
    wordLength = input("\nFirst, decide what is the maximum length of the Wordle word that you will have to guess. \nPlease enter a number ONLY for this: ")
    while wordLength.isdigit() == False:
        wordLength = console.input("[red on yellow]You have not entered a number. Please try again:[/]")
    else:
        return wordLength


def get_random_word(length):
    with open('animals.txt') as animals:
        word_list = [
            line.lower().strip() for line in animals.readlines()
            if (len(line) - 1) == int(length) and all(letter != " " for letter in line)
        ]
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
    print("\n5")


def show_guesses(guesses, word):
    letters_status = {letter: letter for letter in ascii_uppercase}
    for guess in guesses:
        styled_guess = []
        for letter, correct in zip(guess, word):
            if letter == correct:
                style = "bold white on green"
            elif letter in word:
                style = "bold white on yellow"
            elif letter in ascii_letters:
                style = "white on #666666"
            else:
                style = "dim"
            styled_guess.append("[{}]{}[/]".format(style, letter.upper()))
            if letter.upper() != "_":
                letters_status[letter.upper()] = "[{}]{}[/]".format(style, letter.upper())

        console.print("".join(styled_guess), justify = "center")
    console.print("\n" + "".join(letters_status.values()), justify = "center")


def refresh_page(headline):
    console.clear() #clear screen
    console.rule("[bold blue]:leafy_green: {} :leafy_green:[/]\n".format(headline)) # print headline on top of screen -- rule = horizontal rule for decoration


def game_over(guesses, word, correctly_guessed):
    refresh_page("Game Over")
    show_guesses(guesses, word)
    if correctly_guessed:
        print("\nYou won! You got correctly guessed the Wyrdle word!")
    else:
        print("You lost! The Wyrdle word was: {}".format(word))



if __name__ == "__main__":
    main()

