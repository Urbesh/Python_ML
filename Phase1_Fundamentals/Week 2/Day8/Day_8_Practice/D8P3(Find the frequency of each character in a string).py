#Find the frequency of each character in a string
count={}
letters=[]
word=input("Enter a word: ")
for i in word:
    letters.append(i)
for j in letters:
    keys=j
    alph_count=letters.count(j)
    values=alph_count
    count[keys]=values
print(f"The number of times each letter appeared in the word, {word}: ")
print(count)