# Importing functions from other modules
import math

print(math.sqrt(4))

# Function
def myFun1(x):
  print("x: ", x)

myFun1(10)

# Function with default argument value
def myFun2(x=50):
  print("x: ", x)

myFun2()

# Function with keyword arguments
def myFun3(x, y):
  print("x: ", x)
  print("y: ", y)

myFun3(x=10, y=20)

# Arbitrary Keyword Arguments - variable length non-keywords argument
def myFun4(*argv):
  for arg in argv:
    print(arg)

myFun4('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# Arbitrary Keyword Arguments - variable length keyword arguments
def myFun5(**kwargs):
  for key, value in kwargs.items():
    print("%s == %s" % (key, value))

myFun5(first='Geeks', mid='for', last='Geeks')

# Anonymous function
cube = lambda x : x*x*x

print(cube(7))

# Recursive function
def factorial(n):
  if n == 0:  
    return 1
  else:
    return n * factorial(n - 1) 
      
print(factorial(4))