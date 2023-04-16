from time import sleep
from tqdm import tqdm

for i in tqdm(range(100)):
  sleep(.1)
print("Success :D")

cars = [
  "Audi",
  "Volkswagen",
  "Toyota",
  "Nissan",
  "Ford",
  "Subaru",
  "Ikco"
]

cars2 = list()

for car in cars:
  if car[-2:] in ["an", "en"]:
    cars2.append(car)

print(cars2)

cars2 = [
  car for car in cars \
  if car[-2:] in ["an", "en"]
]
print(cars2)