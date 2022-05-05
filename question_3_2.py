def word_scores(word):
    wordscore = 0
    for i in word:
        if i in "EAIORTLSU":
            wordscore += 1
        elif i in "DG":
            wordscore += 2
        elif i in "BCMP":
            wordscore += 3
        elif i in "FHVWY":
            wordscore += 4
        elif i in "K":
            wordscore += 5
        elif i in "JX":
            wordscore += 8
        else:
            wordscore += 10
    return wordscore


result2 = word_scores("SRIJAN")
print(result2)