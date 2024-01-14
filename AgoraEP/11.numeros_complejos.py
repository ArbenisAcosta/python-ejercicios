print('*** Calculador de ecuación de Segundo grado ***')



a = float(input('Digite el valor de a: '))
b = float(input('Digite el valor de b: '))
c = float(input('Digite el valor de c: '))

raiz_cuadrada = (b**2 - 4*a*c)**0.5
denominador = 2*a

solución1 = (-b + raiz_cuadrada) / denominador
solución2 = (-b - raiz_cuadrada) / denominador


if solución1.imag != 0 or solución2 != 0:
  print('Hay solución imaginaria')

print(f'''Solución:
      X1: {solución1}
      X2: {solución2}''')
