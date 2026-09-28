import os

saldo = 500
opcion = 0
pin = "1234"
n_operaciones = 0

###############################

def limpiar_pantalla():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')


def esperar_y_limpiar(mensaje):
  print(mensaje)
  input()
  limpiar_pantalla()

###############################

while(opcion != 6):

  # MOSTRAR MENÚ

  print("===== CAJERO AUTOMÁTICO =====\n1. Consultar saldo\n2. Ingresar dinero\n3. Retirar dinero\n4. Consultar número de operaciones\n5. Cambiar PIN\n6. Salir\n")
  print("Elige una opción: ")

  try:
    opcion = int(input())
  except ValueError:
    print("\nOpción inválida!!!\n")

    esperar_y_limpiar("Pulse Enter para volver al MENÚ...")
    
    continue

  # OPCIÓN 1 -> MOSTRAR SALDO

  if(opcion == 1):
    print("Tu saldo actual es: ", saldo)
    print("\n")
    esperar_y_limpiar("Pulse Enter para volver al MENÚ...")

  # OPCIÓN 2 -> INGRESAR DINERO

  elif(opcion == 2):
    print("Cantidad a ingresar: ")

    try:
        ingreso = int(input())
    except ValueError:
      print("\nOpción inválida!!!\n")
    
      esperar_y_limpiar("Pulse Enter para volver al MENÚ...")
      
      continue

    if(ingreso <= 0):
      print("Cantidad ingresada incorrecta")
    else:
      saldo = saldo + ingreso
      n_operaciones = n_operaciones + 1
      print("Dinero ingresado correctamente.\n")

    esperar_y_limpiar("Pulse Enter para volver al MENÚ...")

  # OPCIÓN 3 -> RETIRAR DINERO

  elif(opcion == 3):
    print("Cantidad a retirar: ")

    try:
      retiro = int(input())
    except ValueError:
      print("\nOpción inválida!!!\n")
  
      esperar_y_limpiar("Pulse Enter para volver al MENÚ...")
      
      continue

    if(retiro > saldo or retiro <= 0):
      print("\nSaldo insuficiente o cantidad a retirar incorrecta\n")
    else:
      saldo = saldo - retiro
      n_operaciones = n_operaciones + 1
      print("Dinero retirado correctamente.\n")

    esperar_y_limpiar("Pulse Enter para volver al MENÚ...")

  # OPCIÓN 4 -> CONSULTAR Nº OPERACIONES REALIZADAS

  elif(opcion == 4):
    print("Número de operaciones realizadas: ", n_operaciones, "\n")

    esperar_y_limpiar("Pulse Enter para volver al MENÚ...")

  # OPCIÓN 5 -> CAMBIAR PIN

  elif(opcion == 5):
    print("PIN actual: ")
    pin_actual =input()

    if(pin_actual == pin):
      print("Nuevo PIN: (El PIN debe formarse con 4 dígitos numéricos)")
      pin_nuevo = input()

      if(len(pin_nuevo) != len(pin) or pin_nuevo.isdigit() == False):
        print("Formato del PIN incorrecto")
      else:
        pin = pin_nuevo
        print("PIN cambiado correctamente\n")
        n_operaciones = n_operaciones + 1

    else:
      print("PIN incorrecto\nNo se ha cambiado el PIN")

    esperar_y_limpiar("Pulse Enter para volver al MENÚ...")

  # OPCIÓN 6 -> EXIT

  elif(opcion == 6):
    print("\nGracias por utilizar el cajero. ¡Hasta pronto!\n")

  else:
    print("\nOpción no disponible!!!\n")
    esperar_y_limpiar("Pulse Enter para volver al MENÚ...")