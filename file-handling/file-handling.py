# Read the file 
with open("file.txt", "r") as file:
  lines = file.readlines()
  for line in lines:
    word = line.split()
    print(word)
  file.close()

# Write the file
with open("file.txt", "w") as file:
  file.write("Hello World")
  file.close()

# Append the file
with open("file.txt", "a") as file:
  file.write("Hello World x2")
  file.close()