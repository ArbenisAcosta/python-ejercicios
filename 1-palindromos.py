cadena = input("Introduce una cadena: ")
cadena = cadena.lower()

lista_cadena = list(cadena)

lista_cadena_alReves = list(cadena)
lista_cadena_alReves.reverse()

while " " in lista_cadena:
  lista_cadena.remove(" ")

while " " in lista_cadena_alReves:
  lista_cadena_alReves.remove(" ")


if lista_cadena == lista_cadena_alReves:
  print("La cadena inroducida es un palíndromo.")
else:
  print("La cadena inroducida NO es un palíndromo.")
