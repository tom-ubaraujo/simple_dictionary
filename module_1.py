import json
import difflib
from difflib import get_close_matches

# Loading the data
data = json.load(open("dictionary.json"))

def retrieve_definition(word):
    word = word.lower()
    
    if word in data:
        return data[word]
    elif word.title() in data: #title() convert the word to capitalized
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        action = input(f"Did you mean: {get_close_matches(word, data.keys(), n=1)} instead? [Y or N]: ")
        if (action == "y"):
            return data[get_close_matches(word, data.keys())[0]]
        elif (action == "n"):
            return ("The word doesn't exist, yet!")
        else:
            return ("Sorry, didn't understand the entry. ")

# user input
word_user = input("Enter a word: ")

# Retrieve the definition using the function and print the result
output = retrieve_definition(word_user)

if type(output) == list:
    for item in output:
        print("-",item)
else:
    print("-",output)