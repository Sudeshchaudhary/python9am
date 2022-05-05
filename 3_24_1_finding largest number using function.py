# create a function to find the largest number in a list.
def number(*list):
    larg = list[0]
    for x in list:
        if x > larg:
            larg = x
    return larg


larg = number(2, 3, 4, 5, 9, 15, 20)
print(larg)
