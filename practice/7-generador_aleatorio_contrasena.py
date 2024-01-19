import random, string

caracteres = list(string.ascii_letters + string.digits + "!#@%&")

letras = list(string.ascii_letters)
numeros = list(string.digits)
especiales = list("!#@%&")


tam = int(input("Por favor, introduce un tamaño para la contraseña: "))

if tam < 6 or tam > 16:

  print("Error! Introduce un tamaño entre 6 y 16 caracteres.")

else:

  random.shuffle(caracteres)

  password = []

  password.append(random.choice(letras))
  password.append(random.choice(numeros))
  password.append(random.choice(especiales))

  for i in range(tam-3):
    password.append(random.choice(caracteres))

  random.shuffle(password)

  print("".join(password))
