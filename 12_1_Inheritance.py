# inheritance is a property of oop that establishes parent child relationship.
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


p = Person("Ram", "Shrestha")


# p.printname()


class Student(Person):
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname)
        self.age = age

    def printname(self):
        print(self.firstname, self.lastname, self.age)


s = Student("Hari", "Poudel", "25")
s.printname()
