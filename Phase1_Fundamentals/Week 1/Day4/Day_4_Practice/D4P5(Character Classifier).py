#Character Classifier: Input a character → check if it’s a vowel, consonant, digit, or special symbol.
char=input("Enter a character: ")
if len(char)!=1:
    print("Please enter a single character.")
else:
    if char.isalpha():
        if char.lower() in 'aeiou':
            print(f"{char} is a vowel.")
        else:
            print(f"{char} is a consonant.")
    elif char.isdigit():
        print(f"{char} is a digit.")
    else:
        print(f"{char} is a special symbol.")

