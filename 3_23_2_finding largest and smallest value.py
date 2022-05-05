# write a program to find the largest and smallest item in the list.
x = [100, 3, 4, 150, 30, 20]
largest = x[0]
smallest = x[0]
for number in x:
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number

print("largest number is", largest)
print("smallest number is", smallest)


