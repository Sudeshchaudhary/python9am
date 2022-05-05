# Encapsulation
class Human:
    def __init__(self, x, y):
        self.name = x  # public variable
        self.__city = y  # private variable

    def a(self):
        print(self.__city)


h1 = Human("ram", "ktm")
print(h1.name)
# print(h1.__city) #private instance variable can't be accessed outside the class.
# But can be accessed within anywhere inside the class.
h1.a()
