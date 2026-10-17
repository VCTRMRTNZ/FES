###
# EXERCICIS
###

# Exercici 1: El missatge secret
# Donada la llista següent:
# missatge = ["C", "o", "d", "i", " ", "s", "e", "c", "r", "e", "t"]
# Fent servir slicing i concatenació, crea una llista nova que contingui només
# el missatge "secret".

missatge = ["C", "o", "d", "i", " ", "s", "e", "c", "r", "e", "t"]

llista_nova = missatge[5:]
print(llista_nova)

#####
print("\n----------\n")
#####

# Exercici 2: Intercanvi de posicions
# Donada la llista següent:
# nombres = [10, 20, 30, 40, 50]
# Intercanvia la primera i l'última posició fent servir només l'assignació per índex.

nombres = [10, 20, 30, 40, 50]

temp = nombres[0]

nombres[0] = nombres[4]
nombres[4] = temp

print(nombres)

#####
print("\n----------\n")
#####

# Exercici 3: L'entrepà de llistes
# Donades les llistes següents:
# pa_de_dalt = ["pa de dalt"]
# ingredients = ["pernil", "formatge", "tomàquet"]
# pa_de_sota = ["pa de sota"]
# Crea una llista anomenada entrepa que contingui, en aquest ordre, el pa de dalt,
# els ingredients i el pa de sota.

pa_de_dalt = ["pa de dalt"]
ingredients = ["pernil", "formatge", "tomàquet"]
pa_de_sota = ["pa de sota"]

entrepa = pa_de_dalt + ingredients + pa_de_sota

print(entrepa)

#####
print("\n----------\n")
#####

# Exercici 4: Duplicar una llista
# Donada una llista:
# llista = [1, 2, 3]
# Crea una llista nova que contingui duplicats els elements de la llista original.
# Exemple: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

llista = [1, 2, 3]

nova = llista + llista
print(nova)

#####
print("\n----------\n")
#####

# Exercici 5: Extreure l'element central
# Donada una llista amb un nombre senar d'elements, extreu-ne l'element central
# fent servir slicing.
# Exemple: llista = [10, 20, 30, 40, 50] -> L'element central és 30

llista = ['hola', 3, 24, 2, 'adeu', 'prova', 33, 44, 45]

meitat = len(llista) // 2
print(llista[meitat])

#####
print("\n----------\n")
#####

# Exercici 6: Inversió parcial
# Donada una llista, inverteix-ne només la primera meitat (fent servir slicing
# i concatenació).
# Exemple: llista = [1, 2, 3, 4, 5, 6] -> Resultat: [3, 2, 1, 4, 5, 6]

llista = [1, 2, 3, 4, 5, 6]

meitat = len(llista) // 2
llista = [llista[:meitat][::-1] + llista[meitat:]]
print(llista)
