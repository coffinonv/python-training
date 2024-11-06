####
### Identity Operators
a = 10
b = 20
c = 10

# "is" operator
print(f"{a} is {b} = {a is b}")
print(f"{a} is {c} = {a is c}")

# "is not" operator
print(f"{a} is not {b} = {a is not b}")
print(f"{a} is not {c} = {a is not c}")

####
### Membership Operators
x = 24
y = 20
list = [10, 20, 30, 40, 50]

# "in" operator
print(f"{x} in {list} = {x in list}")
print(f"{y} in {list} = {y in list}")

# "not in" operator
print(f"{x} not in {list} = {x not in list}")
print(f"{y} not in {list} = {y not in list}")

####
### Ternary Operators
a, b = 10, 20

print(a if a < b else b)
