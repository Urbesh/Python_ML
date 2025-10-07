#Use filter() and a lambda to extract words longer than 4 letters.
strings = input("Enter strings separated by spaces: ").split()
long_words = list(filter(lambda s: len(s) > 4, strings))
print("Words longer than 4 letters:", long_words)