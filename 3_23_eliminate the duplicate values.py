# print sum of all items in a list
x = [10, 3, 4, 1, 30, 20]
b = 0
for a in x:
    b = b + a
print(b)

# write a program to eliminate the duplicate values from the list.
x = [4, 3, 7, 5, 5]
newlist = []
for y in x:
    if y not in newlist:
        newlist.append(y)
print(newlist)
