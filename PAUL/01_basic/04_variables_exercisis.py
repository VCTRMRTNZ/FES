###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.

nom = "Router_1"
ubicacio = "Rack_2"
n_ports = 16
estat = True

print(f"Nom del Router: {nom}\nUbicació del Router: {ubicacio}\nNúmero de ports: {n_ports}\nEstà encès: {estat}\n")

# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.

gb_contractats = 20
gb_consumits = 12

gb_restants = gb_contractats - gb_consumits

print(f"Resten {gb_restants} GB")