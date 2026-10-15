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

###
print("\n----------\n")
###

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

###
print("\n----------\n")
###

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

###
print("\n----------\n")
###

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

###
print("\n----------\n")
###

# Exercici 5: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.

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

###
print("\n----------\n")
###

# Exercici 6: Qualitat d'una connexió de xarxa
# Demana la latència en mil·lisegons i el percentatge de paquets perduts.
# Rebutja una latència negativa o una pèrdua fora del rang del 0 % al 100 %.
# Classifica la connexió com a excel·lent si la latència és de 30 ms o menys
# i la pèrdua és de l'1 % o menys; bona si és de 80 ms o menys i la pèrdua és
# del 3 % o menys; acceptable si és de 150 ms o menys i la pèrdua és del 5 %
# o menys; en qualsevol altre cas, deficient.

lat = float(input("Indica la latència de la connexió de xarxa en ms: "))
per = float(input("Indica el percentatge de paquets perduts en %: "))

while (lat > 0 and per >= 0 and per <= 100):
    if (lat <= 30 and per <= 1):
        print("Teniu una connexió Excel·lent!!!")
        break
    elif (lat <= 80 and per <= 3):
        print("Teniu una Bona connexió.")
        break
    elif (lat <= 150 and per <= 5):
        print("Teniu una conneció Acceptable")
        break
    else:
        print("Teniu una connexió Deficient!!!")
        break
else:
    print("Unitats indocades incorrectes o fora de rang")

###
print("\n----------\n")
###

# Exercici 7: Cost mensual d'un pla de dades
# Demana el tipus de pla (bàsic o plus) i el consum mensual en GB.
# El pla bàsic costa 10 € i inclou 10 GB; cada GB addicional costa 1,50 €.
# El pla plus costa 20 € i inclou 30 GB; cada GB addicional costa 0,75 €.
# Rebutja un consum negatiu o un tipus de pla desconegut. Calcula i mostra el
# cost total, tenint en compte que no es cobra l'excés si no se supera el límit.

pla = input("Indica el tipus de plà contractat (bàsic - B o plus - P): ")
consum = float(input("Indica el consum mensual en GB: "))

cost_basic = 10
basic_ad = 1.5
exces_basic = consum - 10

cost_plus = 20
plus_ad = 0.75
exces_plus = consum - 30

cost = 0

while (pla == "B" or pla == "P" and consum >= 0 and exces_basic != 0 and exces_plus != 0):
    if (pla == "B"):
        if (exces_basic >= 0):
            cost = cost_basic + (exces_basic * basic_ad)
            print(f"Excés de {exces_basic} GB")
            print(f"El cost total és de {cost} €")
            break
        else:
            cost = cost_basic
            print(f"El cost total és de {cost} €")
            break
    else:
        if (exces_plus >= 0):
            cost = cost_plus + (exces_plus * plus_ad)
            print(f"Excés de {exces_plus} GB")
            print(f"El cost total és de {cost} €")
            break
        else:
            cost = cost_plus
            print(f"El cost total és de {cost} €")
            break
else:
    print("Pla desconegut o rang de consum incorrecte...")        

###
print("\n----------\n")
###

# Exercici 8: Accés a un compte de client
# Demana si el compte està actiu, si la contrasenya és correcta i si el codi
# de doble verificació és correcte. Demana el codi només si el compte és actiu
# i la contrasenya és correcta. Indica si l'accés es denega perquè el compte
# està desactivat, perquè la contrasenya és incorrecta o perquè falla el codi;
# si totes les comprovacions necessàries són correctes, permet l'accés.

nom_compte = "victor"
contrasenya = "1234"
codi = "4321"
activo = True
contrasenya_ok = True

opcio_1 = input("Indiqui el nom del compte al que vol accedir: ")

if (nom_compte == opcio_1):
    print("Compte actiu")
    activo = True

    if (activo == True):
        opcio_2 = input("Indiqui la contrasenya del seu compte: ")

        if (contrasenya == opcio_2):
            print("Contrasenya vàlida")

            if (contrasenya_ok == True):
                opcio_3 = input("Indiqui el codi per la doble verificació: ")

                if (opcio_3 == codi):
                    print("Codi correcte. Accés validat. Benvingut!")

                else:
                    print("Accés denegat. Codi de doble verificació incorrecte!")

            else:
                print("Accés denegat. Contrasenya incorrecte!")
                contrasenya_ok = False

        else:
            print("Accés denegat. Contrasenya incorrecte!")
            contrasenya_ok = False

    else:
        print("Accés denegat. Compte inactiu!!!")
        activo = False

else:
    print("Accés denegat. Compte inactiu!!!")
    activo = False

###
print("\n----------\n")
###

# Exercici 9: Diagnòstic d'un router
# Demana si el router està encès, si l'indicador LOS del terminal òptic està
# encès i si l'indicador d'Internet del router està encès. Indica primer si
# cal encendre el router; si ja està encès, comprova si cal revisar el cable
# de fibra (LOS encès), si cal contactar amb el proveïdor (Internet apagat) o
# si la connexió funciona correctament. Considera els casos en aquest ordre.

estat_router = input("Indica l'estat del router (ON/OFF): ")
t_los = input("Indica l'estat de l'indicador LOS del terminal òptic (ON/OFF): ")
internet = input("Indica l'estat de l'indicador d'Internet del router (ON/OFF): ")

if (estat_router in ("ON", "OFF") and t_los in ("ON", "OFF") and internet in ("ON", "OFF")):
    if (estat_router == "ON"):
        print("Router ON")

        if (t_los == "OFF"):
            print("Indicador LOS OFF")

            if (internet == "ON"):
                print("Internet ON")
                print("Connexió funcionant correctament!!!")

            else:
                print("Cal contactar amb el proveïdor d'Internet...")
        else:
            print("Cal revisar el cable de fibra...")
    else:
        print("Cal encendre el router...")
else:
    print("Els estats indicats no són correctes...")

###
print("\n----------\n")
###

# Exercici 10: Prioritat d'una incidència de xarxa
# Demana si la incidència afecta un servei crític, el nombre d'usuaris afectats
# i si hi ha una alternativa de connexió disponible. Rebutja un nombre negatiu
# d'usuaris. Assigna prioritat crítica si afecta un servei crític i no hi ha
# alternativa, o si afecta almenys 50 usuaris i no hi ha alternativa; alta si
# afecta almenys 10 usuaris o un servei crític; en qualsevol altre cas, baixa.


servei_critic = input("La incidéncia es tractà d'un servei crític? (SI/NO): ")
u_afectats = int(input("A quant usuaris està afectant?: "))
alternativa = input("Existèix cap alternativa de connexió (SI/NO): ")

if (servei_critic in ("SI", "NO") and alternativa in ("SI", "NO")):
    if (u_afectats >= 0):

        if (servei_critic == "SI" and alternativa == "NO"):
            print("Incidéncia en estat CRÍTIC!!!")
        elif (alternativa == "NO" and u_afectats >= 50):
            print("Incidència en estat CRÍTIC!!!")
        elif (servei_critic == "SI" or u_afectats >= 10):
            print("Incidéncia en estat ALT!")
        else:
            print("Incidència en estat BAIX")

    else:
        print("Nombre d'usuaris afectats fora de rang")
else:
    print("Opcions no indicades correctament...")

###
print("\n----------\n")
###