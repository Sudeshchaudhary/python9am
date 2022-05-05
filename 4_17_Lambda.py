# lambda is used to define anonymous function(function without any name)
# lambda arguments:expression
# Lambda can have any no of arguments but only one expression
# lambda expression does not contain return function
a = lambda x: x + 10
print(a(4))

b = lambda x, y: x + y + 10
print(b(3, 7))

c = lambda i: "hi" + i
print(c("Srijan"))
