#Reverse words in a sentence
sentence=input("Enter a Sentence: ").split()
words=[]
for i in sentence:
    words.append(i)
words.reverse()
rev_sentence=" ".join(words)
print(rev_sentence)