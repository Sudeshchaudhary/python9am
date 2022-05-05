class Employee:
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setSalary(self, salary):
        self.__salary = salary

    def getSalary(self):
        return self.__salary


e1 = Employee()
e1.setName("Ram Shrestha")
e1.setSalary("Thirty Thousand")
print(e1.getName()+" earns "+e1.getSalary())
