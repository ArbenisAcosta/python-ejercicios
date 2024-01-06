#CALCULADORA DE ÍNDICE DE MASA CORPORAL (IMC)

def calcular_imc(altura, peso):

  return peso / altura**2

altura = float(input("Introduce tu altura en metros: "))
peso = float(input("Introduce tu peso en Kilogramos: "))

imc = calcular_imc(altura, peso)
print("{:.2f}".format(imc))

if imc < 18.5:
  print("Peso insuficiente")
elif imc >= 18.5 and imc < 24.9:
  print("Peso Saludable")
elif imc >= 24.9 and imc < 29.9:
  print("Sobrepeso")
elif imc >= 29.9 and imc < 34.9:
  print("Peso Saludable")
else:
  print("Obesidad morbidad")
