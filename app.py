import json
import os

# Library to pull similar words to use input
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

# Save the data as a python dictionary
data = json.load(open("data.json"))

# Takes the user input, normalizes it, and returns the definitions


def get_definition(word):

    word = word.lower()

    if word in data:
        print("{}:\n".format(word.capitalize()))
        return data[word]
        # TODO: Did you mean (list of matches)?
        # Allow user to select one of the matches
        # Return the word and definition the user chooses
    else:
        matches = get_close_matches(word, data.keys())
        if matches:
            if matches[0] in data:
                print("{}:\n".format(matches[0].capitalize()))
                return data[matches[0]]
            else:
                print("{} is not in the dictionary! Please double check your spelling.".format(
                    word.capitalize()))


# Get user input
word = input("Enter word: ")

# Clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Print to the terminal in a human readable fashion
defined = get_definition(word)

# print("{}:\n".format(word.capitalize()))

print_count = 1

if len(defined) > 1:
    for definition in defined:
        print("{}. {}\n".format(print_count, definition))
        print_count += 1
elif len(defined) == 1:
    print("1. {}\n".format(defined[0]))
else:
    print("{} is not in the dictionary! Please double check your spelling.".format(
                    word.capitalize()))
