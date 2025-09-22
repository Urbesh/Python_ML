#Pangram Check → Does a sentence use every alphabet? 
import string
alphabet=set(string.ascii_lowercase)
sentence=input("Enter a sentence: ").lower()
sentence_letter=set(sentence)
if alphabet.issubset(sentence_letter):
    print("The sentence is Pangram")
else:
    print("The sentence is not Pangram")