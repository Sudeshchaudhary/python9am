class Human:
    no_of_hands = "two"  # class variable

    # class variable value is shared by all instances of a class
    # instance variable value is only accessed by the same instance
    def __init__(self, firstname, lastname):
        self.name = firstname + lastname

    def properties(self):
        print(self.name + " has " + self.no_of_hands+" hands")


h1 = Human("Sudesh ", "Chaudhary")
h1.properties()
h2 = Human("Hari ", "Shrestha")
h2.properties()
print(h1.no_of_hands)
print(h2.no_of_hands)
print(h1.name)
print(h2.name)