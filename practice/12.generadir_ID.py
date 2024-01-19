# Generador ID Unico
import random

print('*** Sistema de Generador ID Unico ***')
nombre = input('Cual es tu Nombre?: ')
apellido = input('Cual es tu Apellido?: ')
anho = input('Cual es tu Año de Nacimiento (YYYY)?: ')
aleatorio = random.randrange(0000,9999)

# print(random)
numero_ID = f'{nombre[0:2]}{apellido[0:2]}{anho[2:4]}{aleatorio}'


print(f'''Hola {nombre}, habitante de ciudad gotica!
      Tu nuevo numero de identificacion (ID) generado por el sistema es:
      {numero_ID.upper()}
      Felicidades!''')
