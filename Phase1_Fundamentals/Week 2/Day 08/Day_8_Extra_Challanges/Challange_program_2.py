#Find the most frequent word in a paragraph
Count_Disc={}
paragraph_lines=[]
print("Enter your paragraph (type 'END' on a new line to finish):")
while True:
    line = input()
    if line.upper()=='END':
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
max_key=max(Count_Disc, key=Count_Disc.get)
print(f"The most frequent word in the paragraph is: {max_key}")