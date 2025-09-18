#String Analyzer Tool
#Input a sentence.
#Print:
#Length of string
#Number of vowels & consonants
#Word count
#String reversed
#Whether it’s a palindrome


def string_analyzer():
    sentence = input("Enter a sentence: ")
    
    # Length of string
    length = len(sentence)
    
    # Number of vowels & consonants
    vowels = "aeiouAEIOU"
    num_vowels = sum(1 for char in sentence if char in vowels)
    num_consonants = sum(1 for char in sentence if char.isalpha() and char not in vowels)
    
    # Word count
    words = sentence.split()
    word_count = len(words)
    
    # String reversed
    reversed_sentence = sentence[::-1]
    
    # Whether it’s a palindrome
    is_palindrome = sentence.replace(" ", "").lower() == reversed_sentence.replace(" ", "").lower()
    
    # Print results
    print(f"Length of string: {length}")
    print(f"Number of vowels: {num_vowels}")
    print(f"Number of consonants: {num_consonants}")
    print(f"Word count: {word_count}")
    print(f"Reversed string: {reversed_sentence}")
    print(f"Is palindrome: {'Yes' if is_palindrome else 'No'}")
if __name__ == "__main__":
    string_analyzer()