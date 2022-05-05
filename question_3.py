# 1E,A,I,O,N,R,T,L,S,U  2 D,G  3 B, C,M,P  4 F,H,V,W,Y  5,K  8 J, X  10 Q,Z
def word_score(word):
    wordscrabble = {"EAIONRTLSU": 1, "DG": 2, "BCMP": 3, "FHVWY": 4, "K": 5, "JX": 8, "QZ": 10}
    wordscore = 0
    for i in word:
        for x in wordscrabble.keys():
            if i in x:
                wordscore += wordscrabble[x]
    return wordscore


#result = word_score("ADVENTURES")
#print(result)

