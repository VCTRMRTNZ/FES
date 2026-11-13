###
# EXERCICIS (diccionaris)
###

# Exercici 1: Crear un diccionari
# Crea un diccionari anomenat estudiant amb les claus "nom", "edat" i "assignatures"
# (aquesta última, una llista amb tres assignatures). Imprimeix-lo.

estudiant = {

    "nom": "Victor",
    "edat": "21",
    "assignatura": ["calcul", "FES", "TCiE"]

}

print(estudiant)

#####
print("\n----------\n")
#####

# Exercici 2: Accedir i modificar
# Imprimeix la segona assignatura de l'estudiant i canvia'n l'edat a un valor nou.

print(estudiant["assignatura"][2])

estudiant["edat"] = "22"

print(estudiant["edat"])

#####
print("\n----------\n")
#####

# Exercici 3: Afegir i eliminar
# Afegeix la clau "grau" a l'estudiant i elimina després la clau "edat" amb del.

estudiant["grau"] = "EET"

print(estudiant["grau"])

del estudiant["edat"]

#####
print("\n----------\n")
#####

# Exercici 4: Comprovar claus
# Comprova amb in si existeixen les claus "nom" i "email" i imprimeix el resultat.

print("nom" in estudiant)
print("email" in estudiant)

#####
print("\n----------\n")
#####

# Exercici 5: Recórrer un diccionari
# Recorre el diccionari amb un bucle for i items() i imprimeix cada parella com "clau: valor".

for clau, valor in estudiant.items():
    print(f"{clau}: {valor}")

#####
print("\n----------\n")
#####

# Exercici 6: Comptar paraules
# Donada la llista de paraules:
# paraules = ["sol", "lluna", "sol", "estrella", "lluna", "sol"]
# Crea un diccionari que indiqui quantes vegades apareix cada paraula.

paraules = ["sol", "lluna", "sol", "estrella", "lluna", "sol"]

repeticions = {}
rep = 0

for paraula in paraules:

    rep = paraules.count(paraula)
    repeticions[paraula] = rep

print(repeticions)
