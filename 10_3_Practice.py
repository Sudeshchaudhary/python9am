def exchange(dollar, rate):
    return (dollar * rate)

nepali = exchange(2, 120)
print(nepali)


def exchange(dollar):
    return dollar * 120

nepali_rupees = exchange(2)
print(nepali_rupees)

def person(name,city):
    print(name+" lives in "+city)
person("sudesh", "chitwan")


def a():
    print("hi")
a()
def a():
    print("hello")

def sub(*nos):
    print(nos[0]-nos[2])
sub(10,5,2)