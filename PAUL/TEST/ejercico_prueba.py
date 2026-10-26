
# EXERCISI D'EXÀMEN PARCIAL1 #

dispositius = []
usuaris = []
serveis_critics = []

opcio = 0

while opcio != 5:
    print("\n--- NetSupport ---")
    print("1. Registrar incidencia")
    print("2. Mostrar incidencias")         # IMPRIMIM EL MENÚ
    print("3. Consultar estadístiques")
    print("4. Comprovar prioritat")
    print("5. Sortir")

    try:
        opcio = int(input("Selecciona una opció: ")) # Control d'entrada per numeros
    except ValueError:
        print("Error: introdueix un número.")
        continue

    if opcio == 1:                                      # Aquí mucho mejor asignar una variable extra antes
        dispositiu = input("Nom del dispositiu: ")

        if dispositiu == "":                            # Verificació de caedena buida
            print("Error: el nom no pot estar buit.")
            continue

        try:
            num_usuaris = int(input("Nombre d'usuaris afectats: ")) # Control d'entrada per numeros enters
        except ValueError:
            print("Error: introdueix un número enter.")
            continue

        if num_usuaris <= 0:
            print("Error: ha d'haver-hi almenys un usuari.")
            continue

        servei = input("És un servei crític? (S/N): ").upper() # .upper() cambia a mayusculas

        if servei != "S" and servei != "N":
            print("Error: introdueix S o N.")
            continue

        dispositius.append(dispositiu) # asignem amb els valors que em guardat, ens estalviem borrar la cadena si algun valor es nul o incorrecte
        usuaris.append(num_usuaris)    # aquí tots els valors han passat el control i són correctes
        serveis_critics.append(servei)

        print("Incidència registrada correctament.")

    elif opcio == 2:
        if len(dispositius) == 0:
            print("No hi ha incidències registrades.")
        else:
            i = 0

            while i < len(dispositius):                     # Recorremos la cadena teniendo en cuenta el numero maximo de elementos
                print("\nIncidència", i + 1)                # El + 1 és pq sinó saldria 0, ya que el idx es 0
                print("Dispositiu:", dispositius[i])
                print("Usuaris afectats:", usuaris[i])
                print("Servei crític:", serveis_critics[i])

                i += 1

    elif opcio == 3:
        if len(dispositius) == 0:
            print("No hi ha incidències registrades.")
        else:
            total_incidencies = len(dispositius)
            total_usuaris = 0                       # creem contadors individuals per cada sortida
            incidencies_grans = 0
            i = 0

            while i < len(dispositius):
                total_usuaris += usuaris[i] # sumem tots els usuaris recorrent la cvadena

                if usuaris[i] >= 50:
                    incidencies_grans += 1 # Contador d'incidencies grans

                i += 1

            print("Total d'incidències:", total_incidencies)
            print("Total d'usuaris afectats:", total_usuaris)
            print("Incidències de 50 usuaris o més:", incidencies_grans)

    elif opcio == 4:
        if len(dispositius) == 0:
            print("No hi ha incidències registrades.")
            continue

        try:
            num_incidencia = int(input("Número de la incidència: "))
        except ValueError:
            print("Error: introdueix un número enter.")
            continue

        if num_incidencia < 1 or num_incidencia > len(dispositius): # Control de rang d'incidencies registrades
            print("Error: aquesta incidència no existeix.")
            continue

        index = num_incidencia - 1

        if serveis_critics[index] == "S":
            print("Prioritat: CRÍTICA")
        elif usuaris[index] >= 50:          # Selector de prioritats
            print("Prioritat: ALTA")
        else:
            print("Prioritat: MITJANA")

    elif opcio == 5:
        print("Tancant NetSupport...")

    else:
        print("Error: opció no vàlida.") # Control de opcions no vàlides
