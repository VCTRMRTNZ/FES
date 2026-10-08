###
# EXERCICIS
###

# Exercici 1: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble

rssi = int(input("Indica el nivell de senyal (RSSI) que reps en dBm: "))

if (rssi >= -50 and rssi <= 0):
    print(f"Un valor de {rssi} dBm és Excel·lent")
elif (rssi < -50 and rssi >= -67):
    print(f"Un valor de {rssi} dBm és Bó")
elif (rssi < -67 and rssi >= -75):
    print(f"Un valor de {rssi} dBm és Feble")
elif (rssi < -75):
    print(f"Un valor de {rssi} dBm és Molt Feble")
else:
    print(f"Un valor de {rssi} dBm no és correcte o està fora del rang normal")

# Exercici 2: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.

con_fo = int(input("Indica la potència òptica que reps en dBm: "))

if (con_fo >= -27 and con_fo <= -8):
    print(f"Un valor de {con_fo} dBm és acceptable")
elif (con_fo > -8 and con_fo < 10):
    print(f"Un valor de {con_fo} dBm és massa alt")
elif (con_fo < -27 and con_fo >= -30):
    print(f"Un valor de {con_fo} dBm és massa baix")
else:
    print(f"Un valor de {con_fo} dBm no és correcte o està fora del rang normal")

# Exercici 3: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.

consum = float(input("Indica el consum de dàdes mils en GB de la teva línia: "))
max = 20

if (consum < max and consum >= 0):
    print("El teu consum està dins del límit contractat")
elif (consum > max):
    print(f"El teu consum ha superat el límit de 20 GB en {consum - max} GB")
elif (consum == max):
    print("Has consumit el màxim de dades contractades")
else:
    print("El consum indicat no és correcte")

# Exercici 4: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.

indicador_los = input("Indiqui si l'indicador LOS del terminal óptic està encès (s/n): ")
indicador_internet = input("Indiqui si l'indicador d'Internet del router està encès (s/n): ")

if (indicador_los == 's' and indicador_internet == 's'):
    print("La connexió funciona correctament")
elif (indicador_los == 's' and indicador_internet == 'n'):
    print("Cal comprovar el servei del proveïdor!")
elif (indicador_los == 'n' and indicador_internet == 's'):
    print("Cal revisar el cable de fibra òptica!")
elif (indicador_los == 'n' and indicador_internet == 'n'):
    print("Cal revisar tant el cable de fibra òptica com el sevei del proveïdor!!!")
else:
    print("No ha indicat correctament l'estat dels indicadors")

# Exercici 5: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.

# try:
#     bat_sai = float(input("Indiqui, en percentatge(%), la bateria restant del SAI: "))
# except ValueError:
#     print("Percentatge indicat invàlid")

bat_sai = float(input("Indiqui, en percentatge(%), la bateria restant del SAI (utilitzeu un '.' per determinar la part decimal): "))

if (bat_sai > 100 or bat_sai < 0):
    print("Percentatge indicat fora de rang!!!")
elif (bat_sai <= 100 and bat_sai >= 50):
    print(f"Un percentatge del {bat_sai}% és un nivell suficient")
elif (bat_sai < 50 and bat_sai >= 20):
    print(f"Un percentatge del {bat_sai}% és un nivell baix!")
elif (bat_sai < 20):
    print(f"Un percentatge del {bat_sai}% és un nivell crític!!!")
else:
    print("Percentatge indicat invàlid...")