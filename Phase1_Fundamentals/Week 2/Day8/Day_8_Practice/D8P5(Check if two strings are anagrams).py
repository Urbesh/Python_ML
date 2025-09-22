#Check if two strings are anagrams.
count_1={}
count_2={}
word_1=input("Enter First word: ")
word_2=input("Enter Second word: ")
if word_1.isalpha() and word_2.isalpha():
    for ch in word_1:
        if ch in count_1:
            count_1[ch]+=1
        else:
            count_1[ch]=1
    for ch in word_2:
        if ch is count_2:
            count_2[ch]+=1
        else:
            count_2[ch]=1
    if len(word_1)==len(word_2) and count_1==count_2:
        print("The words are anagram")
    else:
        print("The words are not anagrams")
else:
    print("Invalid Input")