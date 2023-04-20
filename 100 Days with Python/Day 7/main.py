num1 = float(input('num 1: '))
num2 = float(input('num 2: '))
opr  = input('Operación: ')
err  = "operación no definida"

def suma(a,b):
  return a+b

def rest(a,b):
  return a-b

def mult(a,b):
  return a*b

def divi(a,b):
  return a/b

def pote(a,b):
  return a**b

# Don't do this
# if opr == "suma":
#   print(suma(num1, num2))
# elif opr == "rest":
#   print(rest(num1, num2))
# elif opr == "mult":
#   print(mult(num1, num2))
# elif opr == "divi":
#   print(divi(num1, num2))
# elif opr == "pote":
#   print(pote(num1, num2))
# else:
#   print(err)

# Do this
funcs = {
  "suma": suma(num1, num2),
  "rest": rest(num1, num2),
  "mult": mult(num1, num2),
  "divi": divi(num1, num2),
  "pote": pote(num1, num2)
}

print(funcs.get(opr, err))