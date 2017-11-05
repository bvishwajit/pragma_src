import json
from difflib import get_close_matches
dict_data = json.load(open("data.json", "r"))

def find_word(key):
    key=key.lower()
    if key in dict_data:
        return dict_data[key]
    elif len(get_close_matches(key, dict_data.keys())) > 0:
        return "Did you mean %s instead?"%get_close_matches(key,dict_data.keys())[0]
    else:
        return "The word does not exist. Please double check the word!"

word = input("Enter a word:")
print(find_word(word))
