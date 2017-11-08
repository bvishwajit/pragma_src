import json
from difflib import get_close_matches

#load the file
dict_data = json.load(open("data.json", "r"))

"""
Takes as input a string and returns it definition if the word exists in
English language. Has built-in spelling correction feature.
"""
def find_word(key):
    
    if key in dict_data:
        return dict_data[key]

    key=key.lower()

    if key in dict_data:
        return dict_data[key]
    elif len(get_close_matches(key, dict_data.keys())) > 0:
        yes_no =input("Did you mean %s instead? Enter Y for yes and N for no:"%get_close_matches(key,dict_data.keys())[0])
        if yes_no == "Y":
            return dict_data[get_close_matches(key,dict_data.keys())[0]]
        elif yes_no == "N":
            return "The word does not exist. Please double check the word!"
        else:
            return "Incorrect  choice!"
    else:
        return "The word does not exist. Please double check the word!"

word = input("Enter a word:")
possible_defs = find_word(word)

if type(possible_defs) == list:
    for defs in possible_defs:
        print(defs)
else:
    print(possible_defs)
