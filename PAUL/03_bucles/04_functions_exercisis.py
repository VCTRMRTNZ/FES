###
# EXERCICIS (funcions)
###

# Exercici 1: Funció de salutació
# Crea una funció saludar_a(nom, salutacio="Hola") que imprimeixi la salutació seguida del nom.
# Prova-la amb i sense el segon argument.

def saludar_a(nom, salutació = "Hola"):
    print(f"{salutació} {nom}")

saludar_a("Víctor", "hey")
saludar_a("Víctor")

#####
print("\n----------\n")
#####

# Exercici 2: Parell o senar
# Crea una funció es_parell(numero) que retorni True si el número és parell i False si no ho és.

def es_parell(numero):
    return (numero % 2 == 0)

print(es_parell(2))
print(es_parell(5))

#####
print("\n----------\n")
#####

# Exercici 3: Mitjana d'una llista
# Crea una funció mitjana(numeros) que rebi una llista de números i en retorni la mitjana.
# Fes servir un bucle for.

def mitjana(numeros):
    suma = 0

    for num in numeros:
        suma += num
    return (suma / len(numeros))

print(mitjana ([2, 3, 4, 5, 6]))

#####
print("\n----------\n")
#####

# Exercici 4: Suma amb *args
# Crea una funció sumar_tot(*args) que retorni la suma de tots els números rebuts.
# Prova-la amb 2, 5 i 10 arguments.

def sumar_tot(*args):
    suma = 0
    for numero in args:
        suma += numero
    return(suma)

print(sumar_tot(1, 2))
print(sumar_tot(1, 2, 3, 4, 5))
print(sumar_tot(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

#####
print("\n----------\n")
#####

# Exercici 5: Taula de multiplicar
# Crea una funció taula_multiplicar(numero, limit=10) que imprimeixi la taula de multiplicar
# del número fins al límit indicat, fent servir range().

def taula_multiplicar(numero, limit=10):

    i = 1
    for i in  range(1, limit + 1):
        print(f"{numero} x {i} = {numero * i}")
        i += 1

taula_multiplicar(2)

#####
print("\n----------\n")
#####

# Exercici 6: Informació amb **kwargs
# Crea una funció mostrar_perfil(**kwargs) que imprimeixi cada parella clau: valor.
# Crida-la amb les dades d'un estudiant (nom, edat, grau).

def mostrar_perfil(**kwargs):
    for clau, valor in kwargs.items():
        print(f"{clau}: {valor}")

mostrar_perfil(nom = "victor", edat = 21, grau = "Electrónica de telecos")

#####
print("\n----------\n")
#####

# Exercici 7: Reconvertir exercicis anteriors
# Torna a l'exercici del factorial (while) i del màxim d'una llista (for)
# i converteix-los en funcions que retornin el resultat.

#########
# WHILE #
#########

def factorial(numero):
    resultat = 1

    while (numero > 0):
        resultat *= numero
        numero -= 1

    return(resultat)

print(factorial(3))

#######
# FOR #
#######

def maxim(*args):
    maxim = args[0]

    for num in args:
        if num > maxim:
            maxim = num

    print(f"El maxim és el {maxim}")

maxim(2, 3, 4, 5, 6, 1, 34, 23, 0)
