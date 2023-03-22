#Counting unique letters in a word - Connor

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
  counted_letters = []
  count = 0
  for i in word:
    for letter in letters:
      if counted_letters.count(i) > 0:
        continue
      elif i == letter:
        count += 1
        counted_letters.append(i)
  return count

#print(unique_english_letters("mississippi"))
# should print 4
#print(unique_english_letters("Apple"))
# should print 4

#Code academy answer

def unique_english_letters(word):
  uniques = 0
  for letter in letters:
    if letter in word:
      uniques += 1
  return uniques

def count_char_x(word, char):
    count = 0
    for letter in word:
        if letter == char:
            count += 1
    return count

#print(count_char_x("mississippi", "s"))
#print(count_char_x("mississippi", "m"))

def count_multi_char_x(sentence, char):
    count = 0
    sentence_split = sentence.split(char)
    for split in sentence_split:
        if len(split) > 0:
            count += 1
    return

def count_char(sentence, char):
    count = 0
    counted = sentence.count(char)
    return counted

#print(count_char("Mississippi", "iss"))
#print(count_multi_char_x("doooog", "o"))

#code academy answer
def count_multi_char_x(word, x):
  splits = word.split(x)
  return(len(splits)-1)

def substring_between_letters(word, start, end):
    substring = word[word.index(start):(word.index(end))]
    return substring

#print(substring_between_letters("apple", "p", "e"))

def check_for_name(sentence, name):
    if sentence.count(name) > 0:
        return True
    else:
        return False

#print(check_for_name("My name is Jamie", "Jamie"))

#Code academy answer
def check_for_name(sentence, name):
  return name.lower() in sentence.lower()

#Print every second letter challenge
def every_other_letter(string):
        stripped_string = string.replace(" ", "")
        odd_index_letters = ""
        for x in range(len(stripped_string)):
            if x % 2 == 0:
                odd_index_letters += stripped_string[x]
        return odd_index_letters

#print(every_other_letter("Please print every other letter"))

#Code academy answer
def every_other_letter(word):
  every_other = ""
  for i in range(0, len(word), 2):
    every_other += word[i]
  return every_other

# Reverse function

def reverse_string(word):
    reversed = ""
    for i in range(len(word)):
        reversed += word[-i-1]
    return(reversed)

#print(reverse_string("Turn this inside out"))

#Code academy answer
def reverse_string(word):
  reverse = ""
  for i in range(len(word)-1, -1, -1):
    reverse += word[i]
  return reverse

#Add ! if less than x char
def add_exlamation(string):
    string_plus = string
    while len(string_plus) < 20:
        string_plus += "!"
    return string_plus

#print(add_exlamation("less than 20"))

def sum_values(my_dict):
    sum_vals = 0
    for value in my_dict.values():
        sum_vals += value
    return sum_vals

#print(sum_values({"key1": 2, "key2": 3, "key3": 4}))

def return_even_key_values(my_dict):
    sum_vals = 0
    for key in my_dict.keys():
        if key % 2 == 0:
            sum_vals += my_dict[key]

#print(return_even_key_values({2: 2, 3: 3, 5: 4}))

#Turn list into dict.
def word_length_dictionairy(words):
    empty_dict = {}
    for string in words:
        empty_dict[string] = len(string)
    return empty_dict

list_for_dict = ["wer", "qwe", "rth"]
#print(word_length_dictionairy(list_for_dict))

#Unique values
def unique_values(my_dict):
    my_list = []
    for value in my_dict.values():
        if value not in my_list:
            my_list += [value]
    return len(my_list)

print(unique_values({1: 1, 2: 2, 3: 3}))


class Drivebot:
    def __init__(self):
        self.motor_speed = 0
        self.direction = 0
        self.sensor_range = 0

    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_range):
        self.sensor_range = new_range

robot_1 = Drivebot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

robot_1.control_bot(10, 180)
robot_1.adjust_sensor(20)

print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)