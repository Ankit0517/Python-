import json
from difflib import get_close_matches
data=json.load(open(r'C:\Users\dell\OneDrive\Desktop\data.json'))
def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        print("DID YOU MEAN %S INSTEAD"%get_close_matches(word,data.keys())[0])
        decide=input("PRESS 'y'to confirm")
        if decide=="y":
            return data[get_close_matches(word,data.keys())[0]]
        else: print("WORD NOT FOUND")
        
    else: print("WORD NOT FOUND")    
word=input("ENTER WORD YOU WANT TO SEARCH  ")
output=translate(word)
if type(output)==list:
    for item in output:
        print(item)
else:        
     print(output)    
