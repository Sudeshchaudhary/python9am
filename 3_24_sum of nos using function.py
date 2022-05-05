# Create a function that finds the sum of nos in al ist.
def number(*list):
    a = 0
    for x in list:
        a = x + a
    return a


sum = number(1, 2, 3, 4, 5, 1, 4)
print(sum)
