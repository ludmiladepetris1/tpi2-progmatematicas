import random

def piedra_papel_tijera():
    victorias = 0

    for ronda in range(3):
        print("\n--- Piedra, Papel o Tijera ---")
        print("Ronda", ronda + 1, "de 3\n")

        opcion = input("Escribe piedra, papel o tijera: ").lower()

        if opcion == "piedra":
            jugador = "piedra"
        elif opcion == "papel":
            jugador = "papel"
        elif opcion == "tijera":
            jugador = "tijera"
        else:
            print("Opción inválida")
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
        print("Computadora eligió:", computadora)

        # Decidir ganador
        if jugador == computadora:
            resultado = "Empate"
        elif (jugador == "piedra" and computadora == "tijera") or \
             (jugador == "papel" and computadora == "piedra") or \
             (jugador == "tijera" and computadora == "papel"):
            resultado = "Ganaste"
            victorias += 1
        else:
            resultado = "Perdiste"

        print(resultado)

    print(f"\nPuntuación final: {victorias} victorias")
    
    return victorias

piedra_papel_tijera()
