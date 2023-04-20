# find any of all values
# using list comprehension
values = [-1, 0, 2, 1]
find   = 1

for value in values:
  if value > find:
    print("Encontrado!")
    break
else:
  print("valor no encontrado")

# any and all function
if any(value > find for value in values):
  print("Encontrado!")
else:
  print("valor no encontrado")

if all(value > find for value in values):
  print("Encontrado!")
else:
  print("valor no encontrado")