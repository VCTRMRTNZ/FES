###
# Exercicis - conversió de tipus (casting)
# Completa els exercicis següents convertint dades entre tipus.
###

# Exercici 1
# Demana a l'usuari quants paquets ha rebut un encaminador. Converteix el valor
# introduït a un nombre enter, suma-hi 1200 paquets i mostra el total.

paquets = int(input("Indica quants paquets ha rebut l'encaminador: "))
total_paquets = paquets + 1200

print(f"L'encaminador ha rebut un total de {total_paquets}.\n")

# Exercici 2
# Demana a l'usuari la velocitat d'una connexió en Mbps. Converteix el valor
# introduït a un nombre decimal i calcula la velocitat equivalent en MB/s
# dividint-la per 8. Mostra el resultat.

velocitat = float(input("Indica la velocitat de la connexió en Mbps: "))
v_equivalent = velocitat / 8

print(f"La conversió a MB/s a resultat en {v_equivalent}")
