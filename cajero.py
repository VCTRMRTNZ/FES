saldo = 500
opcion = 0

while(opcion != 4):
  print("===== CAJERO AUTOMÁTICO =====\n1. Consultar saldo\n2. Ingresar dinero\n3. Retirar dinero\n4. Salir\n")
  print("Elige una opción: ")
  opcion = int(input())

  if(opcion == 1):
    print("Tu saldo actual es: ", saldo)
    print("\n")

  elif(opcion == 2):
    print("Cantidad a ingresar: ")
    ingreso = int(input())
    saldo = saldo + ingreso
    print("Dinero ingresado correctamente.\n")

  elif(opcion == 3):
    print("Cantidad a retirar: ")
    retiro = int(input())
    saldo = saldo - retiro
    print("Dinero retirado correctamente.\n")

  elif(opcion == 4):
    print("\nGracias por utilizar el cajero. ¡Hasta pronto!\n")

  else:
    print("\nOpción invàlida!!!\n")
