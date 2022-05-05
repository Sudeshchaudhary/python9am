# if there is an error in the python code, it raises an exception(error).
# if you suspect an error in your code, place the code in try block.
# the try block lets you test a block of code for errors.
# the except block lets you handel the error.

try:
    file = open("d:/abc.txt")
    text = file.read()
    print(text)
# except:
# print("something went wrong when opening the file")

except IOError as error:
    print(error)
else:  # if there is no error in try else also runs.
    print("the file has been read successfully")
finally:
    print("This will run anyhow")

