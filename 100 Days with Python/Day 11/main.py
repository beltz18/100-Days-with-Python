import bcrypt

cadena = "hola".encode("utf-8")
salt   = bcrypt.gensalt()
hashed = bcrypt.hashpw(cadena, salt)
print(hashed)