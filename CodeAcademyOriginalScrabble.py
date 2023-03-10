# Game Title: Scrabble

#Data for functions
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Converting data into dict. & adding "Blank tile" to dict.
letters_to_points = {key:value for key, value in zip(letters, points)}
letters_to_points[""] = 0

#Scrable Functions
def score_word(word):
  points_total = 0
  for letter in word:
    points_total += letters_to_points.get(letter)
  return(points_total)

users_input_score = input("Please enter a word: ")
score_word(users_input_score)

players = ["player1", "wordNerd", "LexiCon", "ProfReader"]
players_words = [["BLUE", "TENNIS", "EXIT"], ["EARTH", "EYES", "MACHINE"], ["ERASER", "BELLY", "HUSKY"], ["ZAP", "COMA", "PERIOD"]]

player_to_words = {key:value for key, value in zip(players, players_words)}

player_to_points = {}

for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

print(player_to_points)
