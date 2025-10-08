#Count vowels and consonants in a string.
#Using String Methods
text=input("Enter a word: ").lower()
vowels="aeiou"
vowels_count=sum(text.count(v) for v in vowels)
consonants_count=sum(text.isalpha() for ch in text)-vowels_count
print(f"The word {text} has {vowels_count} vowel and {consonants_count} consonant")

#Using Flawless's Method
print("Enter a word to check how many vowels and consonants it have")
usr_choice=input("Enter Your Word Here: ").lower()
letters=[]
if usr_choice.isalpha():
    for i in usr_choice:
        letters.append(i)
    vowel=[]
    consonants=[]
    for j in letters:
        if j=="a" or j=="e" or j=="i" or j=="o" or j=="u":
            vowel.append(j)
        else:
            consonants.append(j)
    print(f"The word {usr_choice} have {len(vowel)} vowel and {len(consonants)} consonants")
else:
    print("Invalid Input")
while True:
    opt_to_continue=input("Do you want to check another word (Y/N): ").lower()
    if opt_to_continue=='y':
        usr_choice=input("Enter Your Word Here: ").lower()
        if usr_choice.isalpha():
            letters=[]
            for i in usr_choice:
                letters.append(i)
            vowel=[]
            consonants=[]
            for j in letters:
                if j=="a" or j=="e" or j=="i" or j=="o" or j=="u":
                    vowel.append(j)
                else:
                    consonants.append(j)
            print(f"The word {usr_choice} have {len(vowel)} vowel and {len(consonants)} consonants")
        else:
            print("Invalid Input")
    elif opt_to_continue=='n':
        break
    else:
        print("Invalid Input")


#Update version that can count space, vowels, consonants, Digits, Special Characters 
def text_analyzer(text):
    vowels="aeiou"
    vowel_count=0
    consonant_count=0
    digit_count=0
    space_count=0
    special_count=0

    for ch in text.lower():
        if ch.isalpha():
            if ch in vowels:
                vowel_count+=1
            else:
                consonant_count+=1
        elif ch.isdigit():
            digit_count+=1
        elif ch.isspace():
            space_count+=1
        else:
            special_count+=1

    return vowel_count, consonant_count, digit_count, space_count, special_count
print("Text Analyzer")
while True:
    usr_choice=input("Enter your text: ")
    v, c, d, s, sp=text_analyzer(usr_choice)
    
    print("\nAnalysis Results:")
    print(f"Vowels: {v}")
    print(f"Consonants: {c}")
    print(f"Digits: {d}")
    print(f"Spaces: {s}")
    print(f"Special Characters: {sp}")
    print("-" * 30)

    opt_to_continue = input("Do you want to analyze another text (Y/N): ").lower()
    if opt_to_continue == 'n':
        break
    elif opt_to_continue != 'y':
        print("Invalid Input, try again.")
