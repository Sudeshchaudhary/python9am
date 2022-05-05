# class is a blueprint, class contains function(methods) and properties. we can provide our own class name.
# there can be any number fo methods and properties in class.
# object are instance of class. object is created from the class. object execute the function and acquire
# properties of class.


class human:
    def walk(self):
        print("i am walking")

    def eat(self):
        print("i am eating")

    def sleep(self):
        print("i am sleeping")


dikshya = human()  # creating object or instantiating objects.
shreza = human()
srijan = human()
dikshya.walk()  # object executing methods.
dikshya.eat()
srijan.sleep()


# constructor Function-object create huda run huncha.
# constructor function le object run huda properties lai initialize garcha.
class human():
    def __init__(self, x, y):  # constructor function
        self.name = x  # instance or object variable, object variable ma value initialize gareko.
        self.city = y

    def walk(self):
        print("hi i am " + self.name + " and i live in " + self.city + ".")


a1 = human("ram", "ktm")  # object/instance
a1.walk()
a2 = human("hari", "pkhr")
a2.walk()
