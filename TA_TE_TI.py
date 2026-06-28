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


tablero = ["1", "2", "3",
           "4", "5", "6",
           "7", "8", "9"]

nombre_x = input("Nombre del jugador X: ")
nombre_o = input("Nombre del jugador O: ")

jugador = "X"
turnos = 0

while turnos < 9:

    mostrar_tablero(tablero)

    while True:
        try:
            if jugador == "X":
                posicion = int(input(nombre_x + " (" + jugador + "), elija una posición (1-9): "))
            else:
                posicion = int(input(nombre_o + " (" + jugador + "), elija una posición (1-9): "))

            if posicion >= 1 and posicion <= 9:
                break
            else:
                print("La posición debe estar entre 1 y 9.")

        except:
            print("Debe ingresar un número.")

    if tablero[posicion - 1] != "X" and tablero[posicion - 1] != "O":
        tablero[posicion - 1] = jugador
        turnos += 1

        if ganador(tablero, jugador):
            mostrar_tablero(tablero)

            if jugador == "X":
                print("¡Ganó", nombre_x + "!")
            else:
                print("¡Ganó", nombre_o + "!")
            break

        if jugador == "X":
            jugador = "O"
        else:
            jugador = "X"

    else:
        print("Esa posición ya está ocupada.")

if turnos == 9 and not ganador(tablero, "X") and not ganador(tablero, "O"):
    mostrar_tablero(tablero)
    print("Empate.")


    