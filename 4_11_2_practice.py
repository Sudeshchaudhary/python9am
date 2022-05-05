class Mathdemo:
    def __init__(self, word):
        self.word = word

    def word_score(self):
        wordscrabble = {"EAIONRTLSU": 1, "DG": 2, "BCMP": 3, "FHVWY": 4, "K": 5, "JX": 8, "QZ": 10}
        wordscore = 0
        for i in self.word:
            for x in wordscrabble.keys():
                if i in x:
                    wordscore += wordscrabble[x]
        print(wordscore)


w1 = Mathdemo("ADVENTURES")
w1.word_score()
w2=Mathdemo("SUDESH")
w2.word_score()
