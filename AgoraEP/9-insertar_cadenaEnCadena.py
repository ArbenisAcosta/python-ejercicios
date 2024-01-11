
cadena1 = input("Introduce una cadena de caracteres: ")
cadena2 = input("Introduce otra cadena de caracteres: ")

mitad_cadena = int(len(cadena1)/2)

primera_mitad = cadena1[:mitad_cadena] # [0:5] -> 0,1,2,3,4
segunda_mitad = cadena1[mitad_cadena:] # [0:5] -> 0,1,2,3,4

resultado = f'{primera_mitad}{cadena2}{segunda_mitad}'

print(f'Resultado: {resultado}')
