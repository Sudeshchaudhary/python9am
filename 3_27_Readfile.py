file = open("C:/Users/DELL/Desktop/text.txt", "r")
text = file.read()
# splitted_text = text.split() #converting to the list
splitted_text = list(
    dict.fromkeys(text.split()))  # eliminating duplicate values from list and converting it again list.
splitted_text.sort(reverse=False)  # sorting the list #reverse=True ascending reverse=False Descending

print(splitted_text)


