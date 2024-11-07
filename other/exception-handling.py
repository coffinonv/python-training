# Simple exception handling
try:
  a = 7 / 0
except:
  print("Error")

# Specific exception handling
try:
  a = 7 / 0
except ZeroDivisionError:
  print("Error - Zero division error")

# Try except workflow
try:
  # some code
  pass
except:
  # exception handling
  pass
else:
  # execute if no exception
  pass
finally:
  # always execute at the end
  pass

# Raising exception
try:
  raise NameError("Hi There")
except NameError:
  print("An exception")
  raise