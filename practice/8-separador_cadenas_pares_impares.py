cadena = input("Introduce una cadena de caracteres: ")

# Solición Basica

pares = ""
impares = ""

contador = 0
while contador < len(cadena):

  if contador % 2 == 0:
    impares = impares + cadena[contador]

  else:
    pares = pares + cadena[contador]

    contador += 1

# Solución avanzada

impares2 = cadena[::2]
pares2 = cadena[1::2]

print("Cadena original: " + cadena)
print("Cadena imapres: " + impares)
print("Cadena pares: " + pares)
print("Cadena imapres: " + impares2)
print("Cadena pares: " + pares2)
