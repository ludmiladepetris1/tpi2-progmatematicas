print(" === MULTIVERSO ARCADE === ")

#-------------------------------------------------------------
# FUNCION PARA CADA JUEGO

def escape_monstruo():
    caminos = ["izquierda", "derecha", "recto"]
    pistas = ("Corre rápido", "No mires atrás")
    decisiones = set()

    camino_seguro = random.choice(caminos)

    jugando = True

    while jugando:

        print("\n¡Un monstruo te persigue!")

        for pista in pistas:
            print("-", pista)

        opcion = input("¿Por dónde vas?: ").lower()

        # Significa que se guarda la opcion que eligio el jugador dentro del set
        decisiones.add(opcion)

        if opcion == camino_seguro:
            print("¡Escapaste!")
            print("Ganaste 10 puntos")

            # RESULTADO FINAL:
            # Devuelve 10 puntos al menu, y el menu los suma al ranking.
            return 10

        elif opcion in caminos:
            print("El monstruo te encontró.")

        else:
            print("Ese camino no existe.")

import random

def batalla_naval():

    # MATRIZ 6x6
    matriz = []

    for i in range(6):
        fila = []

        for j in range(6):
            fila.append(0)

        matriz.append(fila)

    # COLOCAR BARCOS
    barcos = 0

    while barcos < 5:

        fila = random.randint(0,5)
        columna = random.randint(0,5)

        if matriz[fila][columna] == 0:
            matriz[fila][columna] = 1
            barcos += 1

    # COMIENZA EL JUEGO
    impacto = 0
    intentos = 0

    while intentos < 10 and impacto < 5:

        print("\nIntento", intentos + 1)

        fila = int(input("Ingrese fila: "))
        columna = int(input("Ingrese columna: "))

        if matriz[fila][columna] == 1:
            print("Impacto")
            matriz[fila][columna] = 0
            impacto += 1

        else:
            print("Agua")

        intentos += 1

    # RESULTADO FINAL

    if impacto == 5:

        # Devuelve 20 puntos al menu, y el menu los suma al ranking.
        return 20

    else:
        # Si pierde obtiene 0 puntos al menu, y el menu los suma al ranking.
        return 0

import random

def piedra_papel_tijera():

    # Empiezas con 0 victorias
    victorias = 0

    while True:
        print("\n--- Piedra, Papel o Tijera ---\n")

        opcion = input("Escribe piedra , papel, tijera o salir: ").lower()

        if opcion == "salir":
            print("Saliendo del juego...")
            print(f"\nPuntuacion final: {victorias} victorias")

        # Se reemplaza el break por el return porque: termina la funcion y devuelve el valor.
        # Cada partida ganada se suma 1 puntos, y hasta que el usuario devida salir del juego
        # se sumara el numero de victorias (puntos) al ranking en el menu.

            return victorias

        if opcion == "piedra":
            jugador = "piedra"
        elif opcion == "papel":
            jugador = "papel"
        elif opcion == "tijera":
            jugador = "tijera"
        else:
            print("Opcion invalida")
            continue

        # Jugada de la computadora
        numero = random.randint(1, 3)

        if numero == 1:
            computadora = "piedra"
        elif numero == 2:
            computadora = "papel"
        else:
            computadora = "tijera"

        print("Tú elegiste:", jugador)
        print("Computadora eligio:", computadora)

        if jugador == computadora:
            print("Empate")
        elif (jugador == "piedra" and computadora == "tijera") or \
             (jugador == "papel" and computadora == "piedra") or \
             (jugador == "tijera" and computadora == "papel"):
            print("Ganaste")
            victorias += 1
        else:
            print("Perdiste")

def mostrar_tablero(tablero):
    print()
    print(tablero[0], "|", tablero[1], "|", tablero[2])
    print("--+---+--")
    print(tablero[3], "|", tablero[4], "|", tablero[5])
    print("--+---+--")
    print(tablero[6], "|", tablero[7], "|", tablero[8])
    print()


def ganador(tablero, jugador):
    return (
        (tablero[0] == jugador and tablero[1] == jugador and tablero[2] == jugador) or
        (tablero[3] == jugador and tablero[4] == jugador and tablero[5] == jugador) or
        (tablero[6] == jugador and tablero[7] == jugador and tablero[8] == jugador) or
        (tablero[0] == jugador and tablero[3] == jugador and tablero[6] == jugador) or
        (tablero[1] == jugador and tablero[4] == jugador and tablero[7] == jugador) or
        (tablero[2] == jugador and tablero[5] == jugador and tablero[8] == jugador) or
        (tablero[0] == jugador and tablero[4] == jugador and tablero[8] == jugador) or
        (tablero[2] == jugador and tablero[4] == jugador and tablero[6] == jugador)
    )

# Entre paréntesis recibe los nombres de los dos jugadores que se ingresaron en el menú.
def ta_te_ti(nombre_x, nombre_o):

    tablero = ["1", "2", "3",
               "4", "5", "6",
               "7", "8", "9"]

    # indica que comienza jugando X.
    jugador = "X"
    # cuenta cuántas jugadas se hicieron.
    turnos = 0

    while turnos < 9:

        mostrar_tablero(tablero)

        # Este ciclo se repite hasta que el jugador ingrese una posición correcta.
        while True:
            try:
                if jugador == "X":
                    posicion = int(input(nombre_x + " (" + jugador + "), elija una posicion (1-9): "))
                else:
                    posicion = int(input(nombre_o + " (" + jugador + "), elija una posicion (1-9): "))

                if posicion >= 1 and posicion <= 9:
                    break
                else:
                    print("La posicion debe estar entre 1 y 9.")

            except:
                print("Debe ingresar un numero.")

        if tablero[posicion - 1] != "X" and tablero[posicion - 1] != "O":

            tablero[posicion - 1] = jugador
            turnos += 1

            # Llama a la función ganador() para comprobar si el jugador actual hizo tres en línea.
            if ganador(tablero, jugador):

                mostrar_tablero(tablero)

                # Si ganó X
                if jugador == "X":
                    return nombre_x, 15
                
                # Si gano O
                else:
                    return nombre_o, 15

            if jugador == "X":
                jugador = "O"
            else:
                jugador = "X"

        else:
            print("Esa posicion ya esta ocupada.")

    mostrar_tablero(tablero)
    print("Empate.")

    return "", 0 

# Escape del Monstruo  devuelve 10 puntos.
# Piedra, Papel o Tijera devuelve la cantidad de victorias.
# Batalla Naval devuelve 20 o 0 puntos.
# Ta-Te-Ti  devuelve 15 puntos si hay un ganador o 0 si hay empate

# ------------------------------------------------------------
# INGRESO NOMBRE DEL JUGADOR

# crea un diccionario vacio; guardar informacion en pares (clave:valor)
# guarda jugador:puntaje

ranking = {}

try:
    with open("ranking.txt", "r") as archivo:
        for linea in archivo:
            jugador, puntos = linea.strip().split(",")
            ranking[jugador] = int(puntos)
except FileNotFoundError:
    pass

nombre = input("Ingrese su nombre: ")

if nombre not in ranking:
    ranking[nombre] = 0

# ------------------------------------------------------------
# MENU INTERACTIVO 

opcion=0

while opcion != 6:

    print("\n - MmENU -")
    print("1. Escape del Monstruo")
    print("2. Piedra Papel o Tijera")
    print("3. Batalla Naval")
    print("4. Ta-te-ti")
    print("5. Ver rankings")
    print("6. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            puntos1= escape_monstruo()
        # sirve para sumar los puntos que gano el jugador en Escapa del monstruo a su puntaje total del ranking
            ranking[nombre] = ranking[nombre] + puntos1

        elif opcion == 2:
            puntos2= piedra_papel_tijera()
        # sirve para sumar los puntos que gano el jugador en Piedra, papel y tijera a su puntaje total del ranking
            ranking[nombre] = ranking[nombre] + puntos2

        elif opcion == 3:
            puntos3= batalla_naval()
        # sirve para sumar los puntos que gano el jugador en Batalla naval a su puntaje total del ranking
            ranking[nombre] = ranking[nombre] + puntos3


        elif opcion == 4:

            nombre_x = input("Nombre del jugador X: ")
            nombre_o = input("Nombre del jugador O: ")

        # Crea una variable para saber si el jugador X/O ya está en el ranking.
         # Empieza en 0, que significa "todavía no lo encontré".
            encontro_x = 0
            encontro_o = 0

            # Recorre todos los nombres que están guardados en el diccionario ranking
            for jugador in ranking:
                if jugador == nombre_x:
                    encontro_x = 1

            # Recorre todos los nombres que están guardados en el diccionario ranking
            for jugador in ranking:
                if jugador == nombre_o:
                    encontro_o = 1

            if encontro_x == 0:
                # Agrega al jugador X al ranking con 0 puntos.
                ranking[nombre_x] = 0

            if encontro_o == 0:
                # Agrega al jugador O al ranking con 0 puntos.
                ranking[nombre_o] = 0

            ganador, puntos = ta_te_ti(nombre_x, nombre_o)

        # Llama a la función ta_te_ti() y le envía los nombres de los jugadores.
        # Se suman los puntos únicamente al jugador que ganó.
            if ganador == nombre_x:
                ranking[nombre_x] = ranking[nombre_x] + puntos

            if ganador == nombre_o:
                ranking[nombre_o] = ranking[nombre_o] + puntos

        elif opcion == 5:
            print("\n - - - RANKING - - -\n")
            lista = []

            for jugador in ranking:
                lista.append([ranking[jugador], jugador])

            for i in range(len(lista)):
                for j in range(i + 1, len(lista)):
                   if lista[i][0] < lista[j][0]:
                      aux = lista[i]
                      lista[i] = lista[j]
                      lista[j] = aux
 
            for datos in lista:
              print(datos[1], "-", datos[0], "puntos")

        elif opcion == 6:
            print(" === MULTIVERSO ARCADE === ")

    except ValueError:
        print("Debe ingresar un número.")

# === GUARDAR RANKING AL SALIR ===

print("\nGuardando ranking...\n")

with open("ranking.txt", "w") as archivo:
    for jugador, puntos in ranking.items():
        archivo.write(f"{jugador},{puntos}\n")