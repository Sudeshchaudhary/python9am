# write a program to print the sum of numbers from 1 to 10.
z = 0
x = 0
while x < 10:
    x += 1
    z = x + z
print(z)

# write a program to count the number of even and odd numbers from 1 to 100.
x = 0
even=0
odd=0
while x < 100:
    x += 1
    if x % 2 == 0:
        even+=1
    else:
        odd+=1
print("even :",even)
print("odd :",odd)

# write a program that prints all the number from 1 to 10 excepts 2 and 5.
x=0
while x<10:

    x+=1
    if x==2 or x==5:
        pass
    else:
        print(x)
