# Scrabble
import enchant

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

#Request numPlayers
while 0 == 0:
  num_players = input("How many players are there?: ")
  if num_players.isdigit():
    num_players = int(num_players)
    break
  else:
    print("\nYou did not enter a number, please make sure you enter a number not letters.\n")

#Add players to list
for player in range(num_players):
  player_input = input("\nPlease enter their names one at a time: ")
  players.append(player_input.title())
  players_words.append([])

#Zip player & word lists
player_to_words = {key: value for key, value in zip(players, players_words)}

#Functions
def add_playerWords():
  for i in range(len(players)):
    print("\n" + players[i] + " please enter a scrabble word: ")
    new_word = input("")
    new_word_upper = new_word.upper()
    d = enchant.Dict("en_Au")
    if d.check(new_word_upper) == True:
      player_words_nested = players_words[i]
      player_words_nested.append(new_word_upper)
      print("\n" + players[i] + " you've earned: " + str(score_word(new_word_upper)) + " points.\n")
    else:
      print("\nThis is not a real word, please make sure you are entering dictionary words only.\n")

def score_word(word):
  points_total = 0
  for letter in word:
    points_total += letters_to_points.get(letter)
  return(points_total)

def point_total_for_allPlayers():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points
  print(player_to_points)

# Main game loop
def main():
  while 0 == 0:
    rounds = input("\nPlease enter the number of rounds that you would like to play (Each player will get one turn per round): ")
    if rounds.isdigit():
      rounds = int(rounds)
      break
    else:
      print("\nYou did not enter a number, please make sure you enter a number not letters.")
  while rounds > 0:
    rounds -= 1
    add_playerWords()
    point_total_for_allPlayers()
  winnersPoints = max(player_to_points.values())
  for key, value in player_to_points.items():
    if value == winnersPoints:
      print("\nCongratulations " + key + " you win! Your final total was " + str(winnersPoints) + " points!")

main()

