import random

# guarda los caminos posibles que el jugador puede elegir
caminos = ["izquierda", "derecha", "recto"]

# ya se las pistas no cambian, aca tiene las pistas del juego
pistas = ("Corre rápido", "No mires atrás")

# va a guardar las decisiones del jugadopr
decisiones = set()

# elije al azarde la lista de caminos
camino_seguro = random.choice(caminos)

jugando = True

#mientras jugando sea verdadero, el juego va aseguir ripientdose
while jugando == True:

    print("\n ¡Un monstruo te persigue!")
    print("Pistas:")

    #recorre cada un de la lista de pistas y lo muesntra por pantalla
    for pista in pistas:
        print("-", pista)

    #deja que el jugador escriba una opcion
    opcion = input("\n¿Por dónde vas? (izquierda, derecha o recto): ").lower()

    #agrega la opcion al set
    decisiones.add(opcion)

    #aca va a ver si el jugador eligio el camino correcto o no
    if opcion == camino_seguro:
        print("Escapaste del monstruo!")
        jugando = False #esto es para darle fin al juego si gano
    
        #el camino no es elc orrecto
    elif opcion in caminos:
        print("El monstruo te encontró! Intenta otra vez.")

    else:
        print("Ese camino no existe.") #por si escriben algo que n sea un izq, derecha o recto

print("\nCaminos que elegiste:") #cuando se termina el while, muestra las decisiones que fueron elegidas
for decision in decisiones:
    print("-", decision)

if jugando == False:
    print(" Fin del juego.") #virifica que el juego temrino S