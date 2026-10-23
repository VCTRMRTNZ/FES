# 📝 Exercicis sobre tuples

# 1️⃣ Crea una tupla amb els noms de 5 ciutats i mostra la segona i la penúltima ciutat.

tupla_1 = ("Barcelona", "Madrid", "València", "Sevilla", "San Sebastián")

print(tupla_1[1])
print(tupla_1[-2])

# 2️⃣ Donada una tupla amb números enters, compta quantes vegades apareix el número 3 a la tupla.

tupla_2 = (1, 2, 3, 3, 3, 4, 5, 3, 4, 5)

rep = tupla_2.count(3)

print(f"El número 3 es repeteix {rep} vegades")

# 3️⃣ Crea una funció que rebi una tupla amb números i retorni una tupla nova amb els números ordenats de menor a major.

def ordenar_tupla(tupla_3):

    llista_3 = list(tupla_3)

    llista_3.sort()

    tupla_3 = tuple(llista_3)

    return(tupla_3)

print(ordenar_tupla((9, 8, 3, 4, 2, 6, 7, 5, 1)))
