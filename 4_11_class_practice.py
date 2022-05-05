class Human():
    def __init__(self, eat, other):
        self.eat = eat
        self.other = other


class Male(Human):
    def __init__(self, eat, other):
        super().__init__(eat, other)

    def rameats(self):
        print("Ram eats", self.eat+".")

    def ramshaves(self):
        print("Ram shaves", self.other+".")


Ram = Male("Food", "Beard")
Ram.rameats()
Ram.ramshaves()


class Female(Human):
    def __init__(self, eat, other):
        super().__init__(eat, other)

    def sitaeats(self):
        print("Sita eats", self.eat+".")

    def sitacombs(self):
        print("Sita Combs", self.other+".")


Sita = Female("Food", "Hair")
Sita.sitaeats()
Sita.sitacombs()
