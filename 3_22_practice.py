list = [3, 5, 8, 7, 2]
count = 1
oddlist = []
evenlist = []
oddno=[]
evenno=[]
length = len(list)
for x in list:
    if count % 2 != 0:
        oddlist.append(x)
    if count % 2 == 0:
        evenlist.append(x)
    if x%2!=0:
        oddno.append(x)
    if x%2==0:
        evenno.append(x)

    count += 1

print(oddlist)
print(evenlist)
print(oddno)
print(evenno)