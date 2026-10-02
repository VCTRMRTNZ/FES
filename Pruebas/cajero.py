import os

saldo = 500
opcion = 0
pin = "1234"
n_operaciones = 0

###############################
#   DEFINICIÓN DE FUNCIONES   #
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

def consultar_saldo(saldo):
  print(f"Tu saldo actual es: {saldo:.2f} €\n")

def ingresar_dinero(saldo, n_operaciones):
  print("Cantidad a ingresar: ")
  
  try:
    ingreso = float(input().replace(",", "."))

  except ValueError:
    print("\nOpción inválida!!!\n")

    return saldo, n_operaciones
  
  if(ingreso <= 0):
    print("Cantidad ingresada incorrecta")
  else:
    saldo += ingreso
    n_operaciones += 1
    print("Dinero ingresado correctamente.\n")

  return saldo, n_operaciones

def retirar_dinero(saldo, n_operaciones):
  print("Cantidad a retirar: ")
  
  try:
    retiro = float(input().replace(",", "."))
  except ValueError:
    print("Opción inválida!!!\n")

    return saldo, n_operaciones
  
  if(retiro > saldo or retiro <= 0):
    print("Saldo insuficiente o cantidad a retirar incorrecta\n")
  else:
    saldo -= retiro
    n_operaciones += 1
    print("Dinero retirado correctamente.\n")

  return saldo, n_operaciones

def consultar_operaciones(n_operaciones):
  print(f"Número de operaciones realizadas: {n_operaciones}\n")

def cambio_pin(pin, n_operaciones):
  pin_actual = input("PIN actual")
  
  if(pin_actual == pin):
    print("Nuevo PIN: (El PIN debe formarse con 4 dígitos numéricos)")
    pin_nuevo = input()
  
    if(len(pin_nuevo) != len(pin) or pin_nuevo.isdigit() == False):
      print("Formato del PIN incorrecto")
    else:
      pin = pin_nuevo
      print("PIN cambiado correctamente\n")
      n_operaciones += 1
  
  else:
    print("PIN incorrecto\nNo se ha cambiado el PIN")

  return pin, n_operaciones

###############################
#      FUNCION PRINCIPAL      #
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
    consultar_saldo(saldo)
    esperar_y_limpiar("Pulse Enter para volver al MENÚ...")

  # OPCIÓN 2 -> INGRESAR DINERO

  elif(opcion == 2):
    saldo, n_operaciones = ingresar_dinero(saldo, n_operaciones)
    esperar_y_limpiar("Pulse Enter para volver al MENÚ...")

  # OPCIÓN 3 -> RETIRAR DINERO

  elif(opcion == 3):
    saldo, n_operaciones = retirar_dinero(saldo, n_operaciones)
    esperar_y_limpiar("Pulse Enter para volver al MENÚ...")

  # OPCIÓN 4 -> CONSULTAR Nº OPERACIONES REALIZADAS

  elif(opcion == 4):
    consultar_operaciones(n_operaciones)
    esperar_y_limpiar("Pulse Enter para volver al MENÚ...")

  # OPCIÓN 5 -> CAMBIAR PIN

  elif(opcion == 5):
    pin, n_operaciones = cambio_pin(pin, n_operaciones)
    esperar_y_limpiar("Pulse Enter para volver al MENÚ...")

  # OPCIÓN 6 -> EXIT

  elif(opcion == 6):
    print("Gracias por utilizar el cajero. ¡Hasta pronto!\n")

  else:
    print("Opción no disponible!!!\n")
    esperar_y_limpiar("Pulse Enter para volver al MENÚ...")
