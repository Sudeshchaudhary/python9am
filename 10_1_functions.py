#function
def a():
    print("hi")
    
a()

def a(*a):
    total = 0
    for x in a:
        total += x
    return total


b = a(10, 20, 30)
print(b)