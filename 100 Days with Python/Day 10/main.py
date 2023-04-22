from uuid import uuid4

users = [
  {
    'id': uuid4(),
    'name': 'Mario',
    'color': 'Red'
  },
  {
    'id': uuid4(),
    'name': 'Luigi',
    'color': 'Green'
  },
  {
    'id': uuid4(),
    'name': 'Peach',
    'color': 'Pink'
  },
  {
    'id': uuid4(),
    'name': 'Bowser',
    'color': 'Yellow'
  },
]

for user in users:
  for k,v in user.items():
    print(f'{k}: {v}')
  print('\n')