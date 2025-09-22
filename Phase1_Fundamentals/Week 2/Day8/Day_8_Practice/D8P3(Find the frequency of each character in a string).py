#Find the frequency of each character in a string
count={}
word=input("Enter a word: ")
for ch in word:
    if ch in count:
        count[ch]+=1
    else:
        count[ch]=1
print(f"The number of times each letter appeared in the word, {word}: ")
print(count)