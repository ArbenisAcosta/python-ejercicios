cadena = input("introduce una cadena de caracter:")
cadena = cadena.lower()


caracteres = {}

for caracter in cadena:

  if caracter in caracteres.keys():
    caracteres[caracter] += 1
  else:
    caracteres[caracter] = 1


print(caracteres)
