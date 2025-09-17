#Palindrome Checker Input: "madam" → Output: Palindrome.
name = input("Enter a word: ")
if name == name[::-1]:
    print(f"{name} is a Palindrome.")
else:
    print(f"{name} is not a Palindrome.")