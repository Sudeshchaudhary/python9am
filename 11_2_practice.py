class Bird:
    def __init__(self, x, y):
        self.name = x
        self.fly = y

    def call(self):
        print("hi my name is " + self.name + " and i can fly " + self.fly + " above")


pigeon = Bird("pigeon", "1 km")
pigeon.call()
eagle = Bird("eagle", "5 km")
eagle.call()


class Person():
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def info(self):
        print("Hi my name is " + self.name + " , I am " + self.age, " years old." + " I lives in " + self.city + ".")


p1 = Person("sudesh", "28", "kathmandu")
p1.info()
p2 = Person("Hari", "25", "Chitwan")
p2.info()
