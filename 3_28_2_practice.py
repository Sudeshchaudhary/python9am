def word_in_letters(word, letters):
    a = list(word)
    b = list(letters)
    count = 0
    for x in b:
        if x in a:
            count += 1
        else:
            count -= 1
    if count == len(a):
        return ("True")
    else:
        return ("False")


# mistake cha program
z = word_in_letters("abb", "aab")
print(z)
