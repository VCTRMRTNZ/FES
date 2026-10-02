###
# exercicis-basics.py
# Exercicis per practicar els conceptes apresos a les lliçons.
###

print("\nExercici 1: Imprimir missatges")
print("Escriu un programa que imprimeixi el teu nom i la teva ciutat en línies separades.")

### Completa aquí

print("Víctor Martínez")
print("Badalona")

print("--------------")

print("\nExercici 2: Mostra els tipus de dades de les variables següents:")
print("Utilitza la comanda 'type()' per determinar el tipus de dades de cada variable.")

a = 15
b = 3.14159
c = "Hola món"
d = True
e = None

### Completa aquí

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print("--------------")

print("\nExercici 3: Conversió de tipus")
print("Converteix la cadena \"12345\" a un enter i després a un float.")
print("Converteix el float 3.99 a un enter. Què passa?")

### Completa aquí

cadena = "12345"

print(int(cadena))
print(float(cadena))
print(f"{int(3.99)}\nEn el cas del 3.99, podem veure que al fer la conversió s'aplica un truncament")

print("--------------")

print("\nExercici 4: Variables")
print("Crea variables per al teu nom, edat i alçada.")
print("Utilitza f-strings per imprimir una presentació.")

# "Hola! Em dic Marc, tinc 38 anys i faig 1.75 metres"
#name = "Marc"
#age = 38

### Completa aquí

name = "Víctor"
age = 21
height = 1.82

print(f"Hola! Em dic {name}, tinc {age} anys i faig {height} metres d'alçada")

print("--------------")

print("\nExercici 5: Nombres")
print("1. Crea una variable amb el nombre PI (sense assignar una variable)")
print("2. Arrodoneix el nombre amb round()")
print("3. Fes la divisió entera entre el nombre resultant i el nombre 2")
print("4. El resultat hauria de ser 1")

### Completa aquí

PI = 3.1416
print(f"El resultat d'arrodinir PI(3.1416) i després dividir-ho entre 2 és: {round(PI) / 2}")

print("--------------")

print("\nExercici 6: Conversor de temperatura")
print("Demana a l'usuari una temperatura en graus Celsius.")
print("Converteix aquest valor a Fahrenheit amb la fórmula: F = (C * 9/5) + 32")
print("Mostra els dos valors amb un missatge clar.")

### Completa aquí

temperatura_celsius = int(input("Introdueix un temperatura en graus Celsius: "))
temperatura_fahrenheit = ((temperatura_celsius * 9)/5) + 32

print(f"La temperatura en graus Celsius és: {temperatura_celsius} ºC\nLa temperatura en graus Fahrenheit és: {temperatura_fahrenheit} F")

print("--------------")

print("\nExercici 7: Calculadora de propina")
print("Demana el total d'un compte i el percentatge de propina.")
print("Calcula quant és la propina i el total final que s'ha de pagar.")
print("Mostra els resultats amb 2 decimals.")

### Completa aquí

total_compte = float(input("Introdueix el valor del compte a pagar en €: "))
p_propina = float(input("Introdueix el percentatge de propina en %: "))

propina = (total_compte * p_propina) / 100

total = total_compte + propina

print(f"El total del compte ha estat: {total_compte} €")
print(f"El percentatge de propina és: {p_propina} %")
print(f"La propina ha pagar són: {propina} €")
print(f"El TOTAL a pagar és: {total} €")

print("--------------")

print("\nExercici 8: Validador de contrasenya simple")
print("Demana una contrasenya a l'usuari.")
print("Comprova si té almenys 8 caràcters.")
print("Mostra 'Contrasenya vàlida' o 'Contrasenya no vàlida'.")

### Completa aquí

contrasenya = str(input("Introdueix una contrasenya d'un mínim de 8 caràcters: "))

if(len(contrasenya) >= 8):
    print("Contrasenya vàlida")
else:
    print("Contrasenya invàlida")