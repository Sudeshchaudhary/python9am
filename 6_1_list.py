# list is  collection
# if we want to store multiple data values at a time, we use list
# along with lost we use other data types such as tuple, set, dictionary to store data.
# we use square brackets in list.
# the index of list starts with 0
# we can add, remove, items from the list.
# items added to its are placed at last.
# list allows duplicate values.

fruits = ["apple", "banana", "carrot"]  # square brackets for list
numbers = [7, 10, 20]
print(fruits)

# list values are accessed using index
#print(fruits[0])
#print(fruits[2])

fruits.append("dragon")
print(fruits)

fruits.insert(2, "cucumber")  # inserting a new item to a list

fruits.insert(0, "graps")
print(fruits)
print(len(fruits))

#fruits.pop(1)  # pop remove specified index from list
#print(fruits)
# del fruits #del deletes the list
# print(fruits)
# fruits.clear()  # clears all the items from the list
# print(fruits)
# fruits.remove("dragon")
# print(fruits)

# print(len(fruits))  # print the length of the list
#print(fruits[-2])  # negative indexing will start from last

#print(fruits[1:3])  # Specify ranges from 1 to 3, excluding 3
#print(fruits[:4])  # gives a range from 0 to 4, excluding 4
#print(fruits[2:])
#print(fruits[-3:-1])

print(fruits[:5])