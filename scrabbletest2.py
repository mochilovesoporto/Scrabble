# Game Title: Scrabble

#Data for functions
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
players = ["player1", "wordNerd", "LexiCon", "ProfReader"]
players_words = [["BLUE", "TENNIS", "EXIT"], ["EARTH", "EYES", "MACHINE"], ["ERASER", "BELLY", "HUSKY"], ["ZAP", "COMA", "PERIOD"]]

# Converting data into dict. & adding "Blank tile" to dict.
letters_to_points = {key:value for key, value in zip(letters, points)}
letters_to_points[""] = 0

#Variables
players_and_words = {key:value for key, value in zip(players, players_words)}
player_to_points = {}

#Scrable Functions
def score_word(word = input("Please enter a word: ")):
    points_total = 0
    for letter in word:
        points_total += letters_to_points.get(letter)
    return(points_total)
    print("Your word has a score of\: " + str(points_total))

def update_player_score():
    for player, words in players_and_words.items():
      player_points = 0
      for word in words:
        player_points += score_word(word)
      player_to_points[player] = player_points
    print("These are the players current point tallies: " + str(player_to_points))

def main():
    score_word()
    update_player_score()

main()