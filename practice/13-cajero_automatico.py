print('*** Cajero automatico de Ciudad Gotica ***')

saldo = 1000 # Saldo inicial
salir = False

while not salir:
  print(f'''Operaciones que puedes realizar:
        1. Consultar saldo
        2. Retirar
        3. Depositar
        4. Salir''')
  opcion = int(input('Escoje una opción: '))

  if opcion == 1:
    print(f'Tu saldo actual  es: ${saldo:.2f}\n')
  elif opcion == 2:
    retirar = float(input('Ingrese el monto a retirar: '))
    # Validadción
    if retirar <= saldo:
      saldo -= retirar # saldo = saldo - retiro, se esta descontado
      print(f'Tu nuevo saldo es: ${saldo:.2f}\n')
    else:
      print(f'No cuentas con suficiente saldo. Saldo actual: {saldo}\n')
  elif opcion == 3:
    deposito = float(input('Ingresa el monto a depositar: '))
    saldo += deposito
    print(f'Tu nuevo saldo es: ${saldo:.2f}')
  elif opcion == 4:
      print('Saliendo del cajero automatico, hasta pronto')
      salir = True
  else:
    print('Opción invalida')
