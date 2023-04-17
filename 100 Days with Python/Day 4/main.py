# Dictionary Comprehensions
names = [
  "Andi",
  "John",
  "Mary"
]
ages = [
  25,
  22,
  21
]

users = {
  names[i]:ages[i] \
  for i in range(len(names))
}

print(users)

# Try Except
msg = "insert number "
num = list()

for i in range(1,3):
  num.append(
    float(input(msg+f'{i}: '))
  )

error = "cannot divide 0"
try:
  result = num[0] / num[1]
except ZeroDivisionError:
  print(error)
else:
  print(f"division is: {result}")