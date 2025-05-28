"""INICIO
1 SE SEBE CREAR UN TABLERO DE X FILA Y X COLUMNAS

2 SE DEBE CREAR DOS PERSONASJES(RATON Y GATO)
  SE DEBE DEFINIR SUS POSICIONES(DONDE EMPIEZAN)
  PONER IDENTIFICADORES A LOS PERSONAJES

3 IMPLEMENTAR MOVIMIENTOS ALEATORIOS

4 IMPLEMENTAR LA LOGICA MINIMAX

5 CREAR COMO SERIA EL JUEGO
"""

import random
import time

columanas = 5
filas = 5 
# Cramos el tablero
def crear_tablero():
    return[["." for c in range(columanas)]for f in range(filas)]

# Motramos el tablero(la creacion del tablero devulve como una lista)
def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))
    print()

#Definimos los movimientos que pueden hacer y que evalue si esta dentro del tablero
def movimientos(fila, columna):
    movimientos = [
        (-1,0), (1,0), (0,-1), (0,1),(-1, -1), (-1, 1), (1, -1), (1, 1) #Movimientos octogonales 
    ]
    movimientos_posibles = []

    for cambio_fila, cambio_columna in movimientos:
        nueva_fila = fila + cambio_fila
        nueva_columna = columna + cambio_columna

        if 0<=nueva_fila<filas and 0<=nueva_columna<columanas:
            movimientos_posibles.append((nueva_fila, nueva_columna))


    return movimientos_posibles

#Definimos movimientos aleatorios dentro de los movimientos que ya definimos
def movimientos_aleatorios(fila, columna):
    movimientos_aleatorios_posibles = movimientos(fila, columna)

    return random.choice(movimientos_aleatorios_posibles)

#Evaluamos la posicion para saber a que distancia se encuentran(Parte del minimax(distancia Manhattan))
def evaluar_posicion(raton_f, raton_c, gato_f, gato_c):
    distancia = abs(raton_f-gato_f) + abs(raton_c - gato_c)
    return -distancia


def minimax(raton_f, raton_c, gato_f, gato_c, profundidad, es_turno_gato):
    
    if raton_f == gato_f and raton_c == gato_c:
        return (1000 if es_turno_gato else -1000), None

    if profundidad == 0:
        return evaluar_posicion(raton_f, raton_c, gato_f, gato_c), None
    
    if es_turno_gato:
        mejor_valor = float("-inf")
        mejor_movimiento = None

        for nueva_f, nueva_c in movimientos(gato_f, gato_c):
            valor, _ = minimax(raton_f, raton_c, nueva_f, nueva_c, profundidad-1, False)
            if valor > mejor_valor:
                mejor_valor = valor
                mejor_movimiento = nueva_f, nueva_c
        return mejor_valor, mejor_movimiento
    
    else:
        mejor_valor = float("inf")
        mejor_movimiento = None

        for nueva_f, nueva_c in movimientos(raton_f, raton_c):
            valor, _ = minimax(nueva_f, nueva_c,gato_f, gato_c, profundidad-1, True)
            if valor < mejor_valor:
                mejor_valor = valor
                mejor_movimiento = nueva_f, nueva_c
        return mejor_valor, mejor_movimiento
    
def juego():

    #Definimos las posiciones de los personajes
    raton_f, raton_c = 0,0
    gato_f, gato_c = filas-1,columanas-1

    turno = 0

    while True:
        if raton_f == gato_f and raton_c == gato_c:
            tablero = crear_tablero()
            tablero[raton_f][raton_c] = "X"
            print(f"Turno{turno}")
            print("El gato trapo al raton")
            mostrar_tablero(tablero)
            break

        if turno == 10:
            tablero = crear_tablero()
            tablero[raton_f][raton_c] = "R"
            tablero[gato_f][gato_c] = "G"
            print(f"Turno{turno}")
            print("El raton escapo del gato")
            mostrar_tablero(tablero)
            break

        tablero = crear_tablero()
        tablero[raton_f][raton_c] = "R"
        tablero[gato_f][gato_c] = "G"
        print(f"Turno {turno}")
        mostrar_tablero(tablero)

        if turno<3:
            new_raton_f, new_raton_c = movimientos_aleatorios(raton_f, raton_c)
            #Actualizamos la posicion
            raton_f, raton_c =  new_raton_f, new_raton_c

            new_gato_f, new_gato_c = movimientos_aleatorios(gato_f, gato_c)
            #Actualizamos la posicion
            gato_f, gato_c =  new_gato_f, new_gato_c

        else:
            _, movimiento_raton = minimax(raton_f, raton_c, gato_f, gato_c, profundidad=4, es_turno_gato = False)
            if movimiento_raton:

                #Actualizamos la posicion
                raton_f, raton_c = movimiento_raton

            _, movimiento_gato = minimax(raton_f, raton_c, gato_f, gato_c, profundidad=4, es_turno_gato = True)
            if movimiento_gato:

                #Actualizamos la posicion
                gato_f, gato_c = movimiento_gato
    
        turno += 1
        time.sleep(0.5)

juego()

            

        

        