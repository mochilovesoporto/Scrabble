# Scrabble

#Print str to user and introduce game as well as game rules
print(''' Hello! Welcome to Scrabble. \n
In Scrabble each letter of the alphabet is assigned a number of points.\n
Players are asked to submit words, these words are then graded and points are awarded to the player. \n
The are 10 rounds to the game, each player may submit one word per round. \n
At the end of the 10 rounds the player with the highest score is the winner! \n
Let's get started!
''')


#Data for creating points system dictionairy
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Converting letters and points lists into dictionairies for function use
letters_to_points = {key:value for key, value in zip(letters, points)}

#Adding "Blank tile" slate to dict.
letters_to_points[""] = 0

#Empty lists/dict.
players = []
players_words = [[]]
player_to_points = {}

#Request number of players to determine how many rounds of the game there are
num_players = int(input("How many players are there?: "))

#For each player that is found in the number of players given to us by the user, ask them to enter their name and add the input to the empty players list, while also creating a new empty list inside players_words to house their words
for player in range(num_players):
  players.append(input("Please enter their names one at a time: "))
  players_words.append([])

player_to_words = {key: value for key, value in zip(players, players_words)}

#Functions

# Create a for loop that loops through each player
# Ask each player for a word,
# Create temporary variable to house invidual players word lists
# Add new word to that players list
# Print each players score for their word
def add_playerWords():
  for i in range(len(players)):
    new_word = input("Please enter a scrabble word: ")
    player_words_nested = players_words[i]
    player_words_nested.append(new_word)
    print(players[i] + "You've earned: " + str(score_word(new_word)) + " points.")

# Takes in word from players_word dict.
# For each letter in that word it gets the associated points allocation from letters_to_points dict & adds it to a temp. variable points_total
# Once loop ends all points from that word are returned to the function
def score_word(word):
  points_total = 0
  for letter in word:
    points_total += letters_to_points.get(letter)
  return(points_total)

# Unzip nest dictionairy
# For each key:value object (players: words) in the players and words dict.
# For each word within the words (values) pass the word into the score_word function
# Store the output of the score_word function (points) in temp var.
# Exit second for loop and pass temp var (points) into player_to_points dict. as a value under each players key
# Print all players and their points
def point_total_for_allPlayers():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points
  print(player_to_points)

# Main game loop
# Loop both functions so that each player gets to input a word 3 times
# Create temp var with 3 rounds
# Create while loop that runs while rounds is greater than zero
# Each loop -= from temp var
# Run functions to ask for words, calculate scores, and add scores to each player
def main():
  rounds = 2
  while rounds > 0:
    rounds -= 1
    add_playerWords()
    point_total_for_allPlayers()

main()

