import re

text="The quick brown fox jumps over the lazy dog"

match = re.search("brown",text)
print(match)
if match:
    print("Match found !")
    print("Start index : ", match.start())

    
    matches=re.findall("the",text,re.IGNORECASE)
    print("Matches : ",matches)
    
    new_text=re.sub("fox","cat",text)
    print("New text",new_text)