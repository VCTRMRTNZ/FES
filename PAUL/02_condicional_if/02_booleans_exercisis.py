###
# EXERCICIS
###

# Exercici 1: Comparar nombres
# Donats els nombres:
# nombre_a = 8
# nombre_b = 5
# Mostra el resultat de comparar si nombre_a és més gran, més petit o igual
# que nombre_b.

nombre_a = 8
nombre_b = 5

print(f"{nombre_a} > {nombre_b}: ", nombre_a > nombre_b)
print(f"{nombre_a} < {nombre_b}: ", nombre_a < nombre_b)
print(f"{nombre_a} = {nombre_b}: ", nombre_a == nombre_b)

#####
print("\n----------\n")
#####

# Exercici 2: Comparar cadenes de text
# Donades les cadenes:
# paraula_a = "Hola"
# paraula_b = "hola"
# Mostra si són iguals i si paraula_a és igual a "Hola".
# Observa si Python distingeix entre majúscules i minúscules.

paraula_a = "Hola"
paraula_b = "hola"

print(f"{paraula_a} = {paraula_b} :", paraula_a == paraula_b)
print(f"{paraula_a} = Hola: ", paraula_a == "Hola")
print(f"{paraula_b} = Hola: ", paraula_b == "Hola")

#####
print("\n----------\n")
#####

# Exercici 3: Connexió de xarxa
# Donats els valors booleans:
# router_encès = True
# connexio_activa = False
# Crea una variable anomenada xarxa_disponible que sigui True només si el
# router està encès i la connexió està activa. Mostra'n el resultat.

router_encès = True
connexio_activa = False

xarxa_disponible = router_encès and connexio_activa

print(xarxa_disponible)

#####
print("\n----------\n")
#####

# Exercici 4: Avisos pendents
# Donats els valors booleans:
# actualitzacio_disponible = False
# alerta_critica = True
# Crea una variable anomenada cal_avisar que sigui True si hi ha una
# actualització disponible o una alerta crítica. Mostra'n el resultat.

actualitzacio_disponible = False
alerta_critica = True

cal_avisar = actualitzacio_disponible or alerta_critica

print(cal_avisar)

#####
print("\n----------\n")
#####

# Exercici 5: Accés a un compte
# Donats els valors booleans:
# compte_actiu = True
# contrasenya_correcta = True
# codi_correcte = False
# dispositiu_de_confiança = True
# compte_bloquejat = False
# Crea una variable anomenada accés_permes que sigui True si el compte està
# actiu, la contrasenya és correcta, el compte no està bloquejat i, a més,
# el codi és correcte o el dispositiu és de confiança. Fes servir and, or i not.
# Mostra'n el resultat.

compte_actiu = True
contrasenya_correcta = True
codi_correcte = False
dispositiu_de_confiança = True
compte_bloquejat = False

acces_permes = ((compte_actiu and contrasenya_correcta) and (codi_correcte or dispositiu_de_confiança) and not compte_bloquejat)

print(acces_permes)
