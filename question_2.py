def word_from_let(word, letters):
    Flag = False
    for i in word:
        if i in letters:
            if (word.count(i) <= letters.count(i)):
                Flag = True
            else:
                Flag = False
            break

        else:
            Flag = False
        break

    return Flag

#result1 = word_from_let("SLAMB", "BMOEALMR")
#print(result1)
#result2=word_from_let("LAMB","BMOEALMR")
#print(result2)