# w - create and save a file
# a - append to an existent file
# r - read a file

text = input("Type something: ")
name = "data.txt"

# Write
with open(name, "w") as file:
  file.write(text)

# Append
with open(name, "a") as file:
  file.write(text+'\n')

# Read
with open(name, "r") as file:
  line = file.read()
  print(line)