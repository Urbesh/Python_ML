#Use map() and a lambda to convert a list of strings to uppercase.
strings=input("Enter strings separated by spaces: ").split()
uppercased=list(map(lambda s: s.upper(), strings))
print("Uppercase list:",uppercased)