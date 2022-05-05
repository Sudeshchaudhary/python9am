def word_from_letters(word, letters):
    count = 0
    for i in word:
        if i in letters:
            if (word.count(i) == letters.count(i)):
                count += 1
            else:
                count -= 1
    if count == len(word):
        aaa = True
    else:
        aaa = False
    return aaa


result2 = word_from_letters("abb", "abb")
print(result2)
