class Human:
    def __init__(self):
        print("this is constructor function of Human")

    def walk(self):
        print("human walking")

    def talk(self):
        print("human talking")


class Male(Human):
    def __init__(self):
        super().__init__()
        print("this is child class constructor of class male")


class Female(Human):
    def talk(self):
        print("female talking")


m1 = Male()  # object create huda constructor function run hunchha afnai constructor function chaina bhane
# parent ko constructor function run huncha.
m1.talk()
f1 = Female()
f1.talk()
