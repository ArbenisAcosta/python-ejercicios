mi_lista = [3, 3, 4, 1, 5, 1, 4, 5, 8, 2, 3]
mi_lista_aux = []

for elemento in mi_lista:
  if elemento not in mi_lista_aux:
    mi_lista_aux.append(elemento)

print("La lista inicial es: ", mi_lista)
print("La lista sin duplicado es: ", mi_lista_aux)
