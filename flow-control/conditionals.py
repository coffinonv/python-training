# If Elif Else statement
a = 5

if a > 5:
  print("a > 5")
elif a < 5:
  print("a < 5")
else:
  print("a = 5")

# Shorthand if statement
i = 10

print(True) if i < 15 else print(False)

# If statement in list comprehension
a = [2,3,4,5]

res = [val ** 2 for val in a if val > 2]
print(res)
