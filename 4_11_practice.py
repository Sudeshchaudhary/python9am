class Human:
    def eat(self, name):
        print(self.name + " eats food.")


class Male(Human):
    def __init__(self, name):
        self.name = name

    def ramshave(self):
        super().eat(self.name)
        print(self.name + " shave beard every morning.")


class Female(Human):
    def __init__(self, name):
        self.name = name

    def sitacomb(self):
        super().eat(self.name)
        print(self.name + " combs hair every morning.")


m1 = Male("Ram")
f1 = Female("sita")
m1.ramshave()
f1.sitacomb()
