# f strings Test
greet = "hello"
name = "Andi"
print(f'{greet:.>7}, my \
      name is {name:.<6}')

# a - ..hello,       my name is Andi.. *
# b - .....hello, my name is Andi.....
# c - .hello, my name is Andi..
# d - ..hello, my name is Andi.

# For Loop Test
cars = [
  'Audi',
  'Volkswagen',
  'Toyota'
]

customers = [
  {
    'name': 'Andi',
    'age': 25
  },
  {
    'name': 'John',
    'age': 22
  },
  {
    'name': 'Mary',
    'age': 21
  },
]
cust_data = []
cust_data.extend(customers)

for i in range(len(cust_data)):
  cust_data['car'] = cars[i] # Way to work: cust_data[i]['car'] = cars[i]

print(cust_data)

# a - property car inside
# dictionary with car value
# b - append car value inside
# list values
# c - new dictionary with only
# car property
# d - TypeError *