#Word Frequency Counter
#Input: a paragraph (string).
#Output: dictionary showing each word and how many times it appears.
#Example:
#Input: "apple banana apple orange banana apple"
#Output: {'apple': 3, 'banana': 2, 'orange': 1}
Count_Disc={}
paragraph_lines=[]
print("Enter your paragraph (type 'END' on a new line to finish):")
while True:
    line = input()
    if line.upper()=='END':  # Using .upper() to make it case-insensitive
        break
    paragraph_lines.append(line)

paragraph="\n".join(paragraph_lines)
print("\nYour paragraph:")
print(paragraph)
words=paragraph.split()
for i in words:
    keys=i
    count=words.count(i)
    values=count
    Count_Disc[keys]=values
print("The number of times each word appeared in the paragraph: ")
print(Count_Disc)