## TEST_01 (PARCIAL 1)

**REVISAR RESPUESTAS, HAY ALGUNAS QUE ESTAN MAL (DICHO POR EL PROFE)**

1. Quina sortida genera aquesta instrucció?

```python
print('Python', 'és', 'brutal', sep='-')
```

A. Python és brutal
B. Python-és-brutal
C. Pythonésbrutal
D. Python,és,brutal

**Resposta correcta: B**

2. Quin tipus de dada té el valor ```1e3``` en Python?

A. int

B. str

C. float

D. complex

**Resposta correcta: C**

3. Quin és el resultat de ```int(3.1416)```?

A. 3

B. 3.14

C. 4

D. Es produeix un ```ValueError```

**Resposta correcta: A**

4. Quin resultat retorna ```bool('False')```?

A. False

B. None

C. Es produeix un error

D. True

**Resposta correcta: D**

5. Què significa que Python tingui tipatge dinàmic?

A. Totes les variables han de declarar el tipus abans d'utilitzar-se.

B. Una mateixa variable pot contenir valors de tipus diferents en moments diferents.

C. Python converteix automàticament qualsevol cadena en un número.

D. Les variables no poden canviar de valor.

**Resposta correcta: B**

6. Quin dels noms següents és un nom de variable vàlid i segueix la convenció utilitzada al repositori?

A. 123_variable

B. el-meu-nom

C. el_meu_nom_de_variable_123

D. el meu nom

**Resposta correcta: C**

7. Amb aquest codi:
```python
pais, ciutat = input().split()
```
Si l'usuari introdueix 'Espanya Barcelona', què imprimiria ```print(f'Vius a {ciutat}, {pais}')```?

A. Vius a Espanya, Barcelona

B. Vius a Barcelona Espanya

C. Vius a Espanya Barcelona

D. Vius a Barcelona, Espanya

**Resposta correcta: D**

8. Quin és el resultat de l'operació següent?
```python
print('100' + str(2))
```

A. 102

B. 1002

C. 100 2

D. TypeError

**Resposta correcta: B**

9. Què passa quan s'executa ```int('Hola món')```?

A. Retorna 0

B. Retorna None

C. Produeix un ValueError

D. Retorna la longitud del text

**Resposta correcta: C**

10. Quin és el resultat d'aquest codi?
```python
edat = 20
edat = 25
print(f'Tinc {edat + 5} anys')
```

A. Tinc 25 anys

B. Tinc 30 anys

C. Tinc edat + 5 anys

D. Tinc 20 anys

**Resposta correcta: B**

11. Quin tipus de dada retorna ```input()``` quan s'introdueix el valor 42?

A. int

B. float

C. bool

D. str

**Resposta correcta: D**

12. Què mostrarà aquest codi?
```python
print('Hola', end='-')
print('món')
```

A. Hola-món

B. Hola         món

C. Hola món

D. Hola--món

**Resposta correcta: A**

13. Considera aquest codi:
```python
edat = 16
te_carnet = True
if edat >= 18 and te_carnet:
    print('Pots conduir')
else:
    print('POLICIA')
```
Què s'imprimeix?

A. Pots conduir

B. POLICIA

C. True

D. No s'imprimeix res

**Resposta correcta: B**

14. Amb ```nota = 7```, i una estructura ```if nota >= 9:``` Excel·lent; ```elif nota >= 7:``` Notable; ```elif nota >= 5:``` Aprovat; ```else:``` No ha aprovat, quin missatge s'imprimeix?

A. Excel·lent!

B. Aprovat!

C. Notable!

D. No ha aprovat!

**Resposta correcta: C**

15. Què passa en aquest fragment?
```python
numero = 0
if numero:
    print('Hola')
```

A. No s'imprimeix Hola perquè 0 s'avalua com a False.

B. S'imprimeix Hola perquè qualsevol número és True.

C. Es produeix un TypeError.

D. S'imprimeix 0.

**Resposta correcta: A**

16. Quin valor tindrà missatge?
edat = 197
missatge = "És major d'edat" if edat >= 18 else "És menor d'edat"

A. 197

B. True

C. És menor d'edat

D. És major d'edat

**Resposta correcta: D**

17. Quin és el resultat de ```'Hola' == 'hola'```?

A. True

B. False

C. hola

D. Depèn del sistema operatiu

**Resposta correcta: B**

18. Donats ```compte_actiu = True```, ```contrasenya_correcta = True```, ```codi_correcte = False```, ```dispositiu_de_confiança = True``` i ```compte_bloquejat = False```, quin resultat dona?
```python
compte_actiu and contrasenya_correcta and (codi_correcte or dispositiu_de_confiança) and not compte_bloquejat
```

A. False

B. None

C. True

D. Es produeix un error

**Resposta correcta: C**

19. En l'exercici de qualitat de connexió, una connexió és bona si ```latencia <= 80 and perdua <= 3```. Quina classificació tindria ```latencia = 80``` i ```perdua = 3```, si no compleix les condicions d'excel·lent?

A. Bona

B. Acceptable

C. Deficient

D. Excel·lent

**Resposta correcta: A**

20. Quina sortida genera el codi següent?
```
x = 10
if x > 5:
    print('A')
elif x > 8:
    print('B')
else:
    print('C')
```

A. B

B. A i B

C. C

D. A

**Resposta correcta: D**

21. Quin resultat té l'expressió següent?
```python
not (True and False) or False
```

A. False

B. True

C. None

D. TypeError

**Resposta correcta: B**

22. Una aplicació ha de mostrar 'Accés permès' només quan edat sigui com a mínim 18 i compte_actiu sigui True. Quina condició és correcta?

A. edat >= 18 or compte_actiu

B. edat > 18 and not compte_actiu

C. edat >= 18 and compte_actiu

D. edat == 18 or not compte_actiu

**Resposta correcta: C**

23. Donada ```fruites = ['pomes', 'peres', 'plàtans', 'maduixes', 'kiwi']```, què retorna ```fruites[-2]```?

A. kiwi

B. plàtans

C. peres

D. maduixes

**Resposta correcta: D**

24. Quin és el resultat de ```nombres = [1, 2, 3, 4, 5]```; ```nombres[1:4]```?

A. [1, 2, 3, 4]

B. [2, 3, 4]

C. [2, 3, 4, 5]

D. [1, 2, 3]

**Resposta correcta: B**

25. Quin resultat retorna ```llista = [1, 2, 3, 4, 5, 6, 7, 8]```; ```llista[1:6:2]```?

A. [1, 3, 5]

B. [2, 3, 4, 5, 6]

C. [2, 4, 6]

D. [1, 3, 5, 7]

**Resposta correcta: C**

26. Què passa si executem?
```python
llista = [1, 2, 3]
llista[10] = 100
```

A. Es produeix un IndexError.

B. Python crea automàticament les posicions intermèdies.

C. El valor 100 s'afegeix al final.

D. La llista no canvia però tampoc es produeix cap error.

**Resposta correcta: A**

27. Què fa el mètode pop() d'una llista?

A. Ordena la llista.

B. Elimina tots els elements.

C. Afegeix un element al final.

D. Elimina un element i retorna el valor eliminat.

**Resposta correcta: D**

28. Quina diferència hi ha entre sort() i sorted() segons els exemples del repositori?

A. No hi ha cap diferència.

B. sort() modifica la llista original, mentre que sorted() pot crear una llista nova ordenada.

C. sorted() només funciona amb números.

D. sort() retorna obligatòriament una tupla.

**Resposta correcta: B**

29. Considera:
```python
original = [1, 2, 3]
copia = original[:]
referencia = original
referencia[0] = 10
```
Quin és el valor d'original?

A. [1, 2, 3]

B. [1, 2, 3, 10]

C. [10, 2, 3]

D. [10, 1, 2, 3]

**Resposta correcta: C**

30. Quin resultat obtenim?
```python
nombres = [1, 2, 3]
nombres.append(4)
nombres.insert(1, 9)
print(nombres)
```

A. [1, 9, 2, 3, 4]

B. [1, 2, 3, 4, 9]

C. [9, 1, 2, 3, 4]

D. [1, 2, 9, 3, 4]

**Resposta correcta: A**

31. Què mostra el codi?
```
animals = ['gos', 'gat', 'gos', 'ocell']
animals.remove('gos')
print(animals)
```

A. ['gat', 'ocell']

B. ['gos', 'gat', 'ocell']

C. ['gos', 'gat', 'gos', 'ocell']

D. ['gat', 'gos', 'ocell']

**Resposta correcta: D**

32. Quin és el resultat?
```python
valors = [3, 1, 3, 2, 3]
print(valors.count(3))
```

A. 2

B. 3

C. 5

D. True

**Resposta correcta: B**

33. En un bucle while, per què és important modificar habitualment la variable utilitzada a la condició?

A. Per evitar que el bucle sigui infinit.

B. Per convertir el while en un for.

C. Per crear una llista.

D. Perquè Python obliga a incrementar sempre les variables.

**Resposta correcta: A**

34. Què imprimeix aquest codi?
```python
comptador = 0
while comptador < 10:
    comptador += 1
    if comptador % 2 == 0:
        continue
    print(comptador)
```

A. 2, 4, 6, 8, 10

B. 0, 2, 4, 6, 8

C. 1, 2, 3, 4, 5

D. 1, 3, 5, 7, 9

**Resposta correcta: D**

35. Què passa amb el bloc else d'un while si el bucle finalitza mitjançant un break?

A. Sempre s'executa abans del break.

B. No s'executa.

C. S'executa dues vegades.

D. Es produeix un error de sintaxi.

**Resposta correcta: B**

36. En el codi:
```python
numero = -1
while numero < 0:
    numero = int(input('Escriu un número positiu: '))
```
Tot i el missatge, quin valor també permet sortir del bucle?

A. -1

B. -100

C. 0

D. Cap: només valors superiors a zero.

**Resposta correcta: C**

37. Què permet obtenir enumerate(fruites) en un bucle com for idx, valor in enumerate(fruites):?

A. Només el valor de cada element.

B. L'índex i el valor de cada element.

C. Només l'índex.

D. La longitud total de la llista.

**Resposta correcta: B**

38. Quin és el resultat?
```python
parells = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]
```

A. [1, 3, 5]

B. [1, 2, 3, 4, 5, 6]

C. [2, 4, 6]

D. [0, 2, 4, 6]

**Resposta correcta: C**

39. Què imprimirà?
```python
fruites = ['poma', 'pera', 'kiwi']
for fruita in fruites:
    if fruita == 'pera':
        break
    print(fruita)
```

A. poma

B. poma, pera

C. kiwi

D. poma, kiwi

**Resposta correcta: A**

40. Quantes vegades s'executa print() en aquest codi?
```python
for lletra in ['A', 'B']:
    for numero in [1, 2, 3]:
        print(lletra, numero)
```

A. 2

B. 3

C. 5

D. 6

**Resposta correcta: D**