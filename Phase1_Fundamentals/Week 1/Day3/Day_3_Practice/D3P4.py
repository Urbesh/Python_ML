#Substring Counter : Count how many times a certain letter appears in a given string. Input: "banana", "a" → Output: 3.
string = input("Enter a string: ")
letter = input("Enter a letter to count: ")
count = string.count(letter)
print(f"The letter '{letter}' appears {count} times in '{string}'.")