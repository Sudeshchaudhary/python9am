# replace hyphens with a single space,
# convert all character to uppercase,
# split hyphenated words in to separate words,
# strip off all contractions and possessives from words: 's,'re, etc,
# remove all punctuation, whitespace characters and numbers,
# only keep words which also occur in the official sow pods list,
# no duplicate the word list.

file = open("C:/Users/DELL/Desktop/text.txt", "r")
text = file.read()
text = text.replace("-", " ")
text = text.split()
for x in range(len(text)):
    text[x] = text[x].upper()


print(text)
