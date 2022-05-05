'''
def dict(**person):
    print(person["name"])
    print(person["city"])


dict(name="sudesh", city="chitwan")


def alphabet(*character):
    for x in character:
        print(x)
        if x == "d":
            break


alphabet("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z")


# 1. set the value of length and breadth and check if it's a rectangle or square.
def a(length, breadth):
    if length == breadth:
        print("it is square")
    else:
        print("it is rectangle")


a(4, 5)


# 2.find the greatest amount 3 nos.
def number(*nos):
    if nos[0] > nos[1] and nos[0] > nos[2]:
        print("nos[0] is greatest among 3")
    elif nos[1] > nos[0] and nos[1] > nos[2]:
        print("nos[1] is greatest among 3")
    elif nos[2] > nos[0] and nos[2] > nos[1]:
        print("nos[2] is greatest among 3")


number(5, 6, 7)


# 3.write a program that allows student ato attend exam if he/she has 75% attendance or only if she has some medical condition.
def student(attendence, medical_condition):
    if attendence >= 75 or medical_condition == True:
        print("you are eligible for exam")
    else:
        print("you are not eligible for exam")


student(74, False)


# 4.mame["ram","shyam","hari"]
# wap that print the following output
# Hello ram
# hello shyam
# hello hari
def name(*name):
    for x in name:
        print("hello", x)


name("ram", "shyam", "hari")

# 5.wirte a rogram that print the following output.
3*1=3
3*2=6
3*4=9
. 
3*10=12



def three(three):
    x = 1
    while x <= 10:
        mul = 1
        mul = three * x
        print(three, "X", x, "=", mul)
        x += 1


three(3)


# 6. write a program that print the no. of occurrence of r in the word parrot and o of occurences of othe letters.

def count(letter):
    count = 0
    oc = 0
    for x in letter:
        if x == "r":
            count += 1
        else:
            oc += 1
    print("occurrence of r is", count, "times")
    print("number of occurrence of other letter is", oc, "times")


count("parrot")

7.
1:odd
2:even
3:odd
4:even
5:odd



def number(*oddeven):
    for x in oddeven:
        if x % 2 == 0:
            print(x, ":", "even")
        else:
            print(x, ":", "odd")


number(1, 2, 3, 4, 5)

8.
hello
hello
hi
hello
hello



def name(*word):
    for x in word:
        if x == 3:
            print("hi")
        else:
            print("hello")


name(1, 2, 3, 4, 5)

name = ["ram", "shyam", "hari"]
for x in name:
    print("hello", x)


#def addition(*a):
    z = a[0] + a[1]
    print(z)


#addition(3, 4)
'''

def addition(*addition):
    z=0
    for x in addition:
        z=z+x
    print(z)


addition(3, 4,1)