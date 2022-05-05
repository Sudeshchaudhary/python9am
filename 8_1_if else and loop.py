x = 3

y = 2
if x > y:
    print(x)
if x == y:
    print("yes")
elif x > y:
    print("x is gater than y")
elif x < y:
    print("x is smaller than y")
else:
    print("no")

grade = "D"
if grade == "A":
    print("Excellent")
elif grade == "B":
    print("good")
elif grade == "C":
    print("satisfactory")
elif grade == "D" or grade == "E":
    print("Poor")
else:
    print("please inter the correct value")

race = "Asian"
age = 20

if race == "Asian" and age > 20:
    print("you are eligible for verocel vaccination")
elif race == "Asian" and age <= 20:
    print("Indian Vaccination")

else:
    print("You are not eligible")

# looping
x = 1
while x <= 10:
    print(x)
    x += 1

y = 10
while y >= 1:
    print(y)
    y -= 1
