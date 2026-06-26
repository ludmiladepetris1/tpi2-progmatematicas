# -----------------------------------------------------------------------------------------
import random
# SE CARGA UNA MATRIZ VACIA DE 6X6:
   # 0 = vacio (agua) 1 = ocupado (barcos)
matriz=[]
for i in range(6):
    filas=[]
    for j in range(6):
        filas.append(0) # se empieza vacio.
    matriz.append(filas)

# -----------------------------------------------------------------------------------------

# COLOCACION DE BARCOS ALEATORIAMENTE
  # nota 1°: import random / permite generar números aleatorios.
  # nota 2°: random.randint(0, 5) / generar un numero aleatorio entre 0 y 5 (porque la matriz es de 6x6)

barcos=0

while barcos < 5:
    fila= random.randint(0,5)
    columna=  random.randint(0,5)

    # Verificamos que no haya barcos en esa posicion
    if matriz[fila][columna] == 0:
        matriz[fila][columna] = 1
        barcos += 1

# -----------------------------------------------------------------------------------------

# SE COMIENZA A JUGAR
impacto=0 # SI encuentra un barco.
intentos=0 # NO encuentra un barco.

while intentos <= 10 and impacto <= 5: 

    print("\nIntento", intentos + 1)

    fila = int(input("Ingrese fila: "))
    columna = int(input("Ingrese columna: "))

     # Verificamos disparos
    if matriz[fila][columna] == 1: # habia barco
        print("Impacto")

        matriz[fila][columna]= 0 # ya no hay mas barco
        impactos += 1
    else:
        print("Agua")

    intentos += 1 

# -----------------------------------------------------------------------------------------

# RESULTADOS DEL JUEGO
if impacto == 5:

    print("\nGanaste. Destruiste todos los barcos")

else:

    print("\nFin del juego")
    print("Barcos destruidos:",impacto)