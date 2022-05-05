x = 10
list = [4, 7, 8, 9]
if x in list:
    print("10 in present in the list")
else:
    print("10 is not present in list")


x = 10
count = 0
list = [4, 7, 8, 9, 10, 3]
for a in list:
    count += 1
    if x in list:
        print("10 in present in the list")
        break
    else:
        if count == len(list):
            print("10 is not present in list")

list = [4, 7, 10, 5, 2]
newlist = []
length = len(list)
while length > 0:
    length = length - 1
    newlist.append(list[length])

print(newlist)


list = [4, 7, 10, 5, 2]
count = 1
oddlist = []
length = len(list)
for x in list:
    if count % 2 != 0:
        print(x)
        oddlist.append(x)

    count += 1

print(oddlist)

