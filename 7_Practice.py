alphabet = {
    "a": "apple",
    "b": "ball",
    "c": "camel",
    "d": "dog",
    "e": "elephant",
    "f": "fan",
    "g": "giraffe",
    "i": "ink"
}
for x in alphabet.values():
    print(x)
'''
a=alphabet.get("a")
b=alphabet.get("b")

print(a)
print(b)

print(alphabet.keys())
alphabet["j"]="jack fruits"
print(alphabet.keys())

alphabet["k"]="kauli"
print(alphabet.values())
print(type(alphabet))
'''
'''
fruits=["apple","banana","cherry","kiwi","mango"]
newlist=[]
for x in fruits:
    if'a' in x:
        newlist.append(x)
print(newlist)
'''
'''
x = [10, 40, 60, 3]
print(x[1])

a = x[1]
print(a)

b = x[3]
print(b)

name = "Sudesh"
for x in name:
    print(x)
'''
mobile = {
    "a" : "apple",
    "s":"sony",
    "m":"mi",
    "o":"oneplus",
    "g":"galaxy"
}
for x in mobile.values():
    print(x)
for x in mobile.keys():
    print(x)

numbers=[9,8,4,2,7,3,9,3,2]
for x in numbers:
    print(x)