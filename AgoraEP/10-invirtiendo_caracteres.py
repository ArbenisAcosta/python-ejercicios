cadena = "Python"

cadena_resultado = ""

# Forma 1
# contador = 1
# while contador <= len(cadena):

# Forma 2
contador = len(cadena) - 1
while contador >= 0:

# Forma 1
  # cadena_resultado = cadena_resultado + cadena[-contador]
# Forma 2
  cadena_resultado = cadena_resultado + cadena[contador]

# Forma1
  # contador += 1

# Forma 2
  contador -= 1

print(f'Cadena original: {cadena}')
print(f'Cadena resultado: {cadena_resultado}')

print('*** ***')

cadena_resultado2 = cadena[-1:-len(cadena)-1:-1]

print(cadena)
print(cadena_resultado2)
