###
# EXERCICIS (for)
###

# Exercici 1: Imprimir números parells
# Imprimeix tots els números parells del 2 al 20 (inclosos) fent servir un bucle for.

for numero in range(2, 21, 2):

    print(numero)

#####
print("\n----------\n")
#####

# Exercici 2: Calcular la mitjana d'una llista
# Donada la llista de números següent:
# numeros = [10, 20, 30, 40, 50]
# Calcula la mitjana dels números fent servir un bucle for.

numeros = [10, 20, 30, 40, 50]
resultat = 0

for num in numeros:
    resultat += num

mitjana = resultat / len(numeros)
print(mitjana)


#####
print("\n----------\n")
#####

# Exercici 3: Buscar el màxim d'una llista
# Donada la llista de números següent:
# numeros = [15, 5, 25, 10, 20]
# Troba el número màxim de la llista fent servir un bucle for.

numeros = [15, 5, 25, 10, 20]
maxim = numeros[0]

for num in numeros:
    if num > maxim:
        maxim = num

print(f"El maxim és el {maxim}")

#####
print("\n----------\n")
#####

# Exercici 4: Filtrar cadenes per longitud
# Donada la llista de paraules següent:
# paraules = ["casa", "arbre", "sol", "elefant", "lluna"]
# Crea una llista nova que contingui només les paraules amb més de 5 lletres
# fent servir un bucle for i list comprehension.

paraules = ["casa", "arbre", "sol", "elefant", "lluna"]

for paraula in paraules:
    if len(paraula) > 5:
        print(paraula)



#####
print("\n----------\n")
#####

# Exercici 5: Comptar paraules que comencen per una lletra
# Donada la llista de paraules següent:
# paraules = ["casa", "arbre", "sol", "elefant", "lluna", "cotxe"]
# Demana a l'usuari que introdueixi una lletra.
# Compta quantes paraules de la llista comencen per aquesta lletra (sense diferenciar majúscules/minúscules).

paraules = ["casa", "arbre", "sol", "elefant", "lluna", "cotxe"]

lletra = input("Inrodueix una lletra a cercar: ")

for paraula in paraules:
    if lletra == paraula[0]:
        print(f"Aquesta paraula comença per la lletra {lletra}: {paraula}")

