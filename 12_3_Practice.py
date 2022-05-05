class Human:
    def __init__(self, x, y):
        self.name = x
        self.city = y

    def walk(self):
        print("Human Can Walk")


class Male(Human):
    def __init__(self):
        # pass
        # print("hi")
        super().__init__("sudesh", "chitwan")
        print("hello")

    def walk(self):
        print("Male Can Walk")
        super().walk()


# super can call parent method
objmale = Male()
objmale.walk()
# objhuman=Human("sudesh","chitwan")
# objhuman.walk()
