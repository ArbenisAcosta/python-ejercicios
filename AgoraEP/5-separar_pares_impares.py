def separar_pares_impares(lista_entrada):

  lista_pares, lista_impares = [], []

  for numero in lista_entrada:

    #Caso de que el número sea par:
    if (numero % 2) == 0:
      lista_pares.append(numero)
    #Caso de que el número sea impar:
    else:
      lista_impares.append(numero)

  return  lista_pares, lista_impares

mi_lista = [2,3,4,5,3,8,20,7,9,15,30,12,22,87]

print("la lista inicial es: ", mi_lista)

lista_pares, lista_impares = separar_pares_impares(mi_lista)

lista_pares.sort()
lista_impares.sort()

print("La sublista de números pares es: ", lista_pares)
print("La sublista de números impares es: ", lista_impares)
