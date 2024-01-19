# Minimo comun multiplo

def mcm(num1, num2):

  if num1 > num2:
    num_mayor = num1
  else:
    num_mayor = num2

    while (num_mayor % num1) != 0 or (num_mayor % num2) != 0:
      num_mayor += 1

    return num_mayor

print(mcm(20, 6))
