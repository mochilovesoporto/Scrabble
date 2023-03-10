# Scrabble

#Data
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
players = ["player1", "wordNerd", "LexiCon", "ProfReader"]
players_words = [["BLUE", "TENNIS", "EXIT"], ["EARTH", "EYES", "MACHINE"], ["ERASER", "BELLY", "HUSKY"], ["ZAP", "COMA", "PERIOD"]]
player_to_points = {}

num_players = int(input("How many players are there?: "))

for player in range(num_players):
  players.append(input("Please enter their names one at a time: "))
  players_words.append([])

# Converting data into dict. & adding "Blank tile" to dict.
letters_to_points = {key:value for key, value in zip(letters, points)}
letters_to_points[""] = 0
player_to_words = {key: value for key, value in zip(players, players_words)}

print(players)
print(players_words)
print(player_to_words)