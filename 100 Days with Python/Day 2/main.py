cadena = input("...")

match cadena:
  case "hola":
    print("hola, ¿qué tal?")
  case "adios":
    print("adios :C")
  case _:
    print(":D")

var = {
  0: "Algo",
  "algo": 0,
  "nada": "nada"
}

print(var["algo"])
print(var["nada"])
print(var[0])
print(var[1])

error = "no existe"
cond = var.get(4, error)
print(cond)