class Student:
    school_name = "ITN"

    def __init__(self, name, course):
        self.name = name
        self.course = course

    def info(self):
        print(self.name + " is studying " + self.course + " at " + self.school_name)


s1 = Student("ram", "python")
s1.info()
s2 = Student("hari", "web_design")
s2.info()
