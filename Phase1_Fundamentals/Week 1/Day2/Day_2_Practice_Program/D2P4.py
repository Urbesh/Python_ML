#Use membership operators: Check if "a" is in "Shoyo"
#I made the program dynamic so the it can accept more words, rather than just the single word "Shoyo"
wod=input("Enter a Word or a Sentence: ")
fid=input("Enter the letter or the word you want to check is it's present or not: ")
if fid in wod:
    print(fid,"is Present")
else:
    print(fid,"is not present")
