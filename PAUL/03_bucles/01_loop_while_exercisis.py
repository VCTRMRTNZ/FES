###
# EXERCICIS (while)
###

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.

numero = 10

while (numero != 0):

    print(numero)
    numero -= 1

#####
print("\n----------\n")
#####

# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.

numero = 1
resultat = 0

while (numero <= 20):
    if (numero % 2 == 0):
        resultat += numero
    numero += 1

print(resultat)

#####
print("\n----------\n")
#####

# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.

numero = int(input("Introdueix un numero enter positiu: "))
resultat = 1

while (numero > 0):
    resultat *= numero
    numero -= 1

print(resultat)

#####
print("\n----------\n")
#####

# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".

contrasenya = input("Introdueix una contrasenya de com a mínim 8 caràcters: ")

print(len(contrasenya))

while (len(contrasenya) < 8 ):
    print("Contrasenya invàlida, torni a provar...")
    contrasenya = input("Introdueix una contrasenya de com a mínim 8 caràcters: ")

print("Contrasenya introduida correcte!!!")

#####
print("\n----------\n")
#####

# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.

numero = int(input("Introdueix un numero: "))
i = 1

while (i <= 10):
    print(f"{numero} x {i} = {numero*i}")
    i += 1

#####
print("\n----------\n")
#####

# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.

n = int(input("Introdueix un numero enter positiu: "))

numero = 2

while (numero <= n):
    primo = True
    divisor = 2
    while (divisor * divisor <= numero):
        if (numero % divisor == 0):
            primo = False
            break
        divisor += 1
    if primo:
        print(numero)
    numero += 1
