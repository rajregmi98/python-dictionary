import json
from difflib import get_close_matches
data = json.load(open ("data.json"))
def translate(w):
    w = w.lower()
    if  w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys()))>0:
        yn = input("did you mean %s intread? enter y if yes or enter n if no" % get_close_matches(w, data.keys())[0])
        if yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "n":
            return "word doesn't exist. please check the word. "
        else:
            return "we don't understand your query."

    else: return "The word don't contain.please check the word."
word = input("enter a word = ")
output = translate(word)
for item in output:
    print (item)
