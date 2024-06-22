import random
import os
import time
from collections import deque


def crear_tablero():
    return [[8, 7, 6], [5, 4, 3], [2, 1, ""]]

def crear_tablero_vacio():
    return [["" for _ in range(3)] for _ in range(3)]

def mostrar_tablero(tablero):
    for fila in tablero:
        print("|", " | ".join(str(x) if x != "" else " " for x in fila), "|")

def encontrar_vacio(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] == "":
                return i, j
#Metodo de BFS
def resolver_ia(tablero):
    # Almacena todo, el tablero, los caminos, y las posiciones de vacio
    Almacen = deque([(tablero, [], encontrar_vacio(tablero))])
    visitados = set()
    #Combierte cada fila en una tupla y luego el tablero en tupla
    visitados.add(tuple(tuple(row) for row in tablero))
    while Almacen:
        #Extrae el primer elemento de la cola para procesarlo
        tablero_actual, camino, (vacio_y, vacio_x) = Almacen.popleft()
        if verificar_ganador(tablero_actual):
            return camino
        direcciones = [1, 2, 3, 4]  # Arriba, Abajo, Derecha, Izquierda
        for direccion in direcciones:
            #Crea un nuevo tablero con las nuevas filas cambiadas
            nuevo_tablero = [fila[:] for fila in tablero_actual]
            if Movimiento(vacio_y, vacio_x, direccion, nuevo_tablero, 2):
                #Lo combierte en dupla el nuevo tablero como el anterior
                estado_tablero = tuple(tuple(row) for row in nuevo_tablero)
                if estado_tablero not in visitados:
                    visitados.add(estado_tablero)
                    #Almacena los nuevos datos
                    Almacen.append((nuevo_tablero, camino + [direccion], encontrar_vacio(nuevo_tablero)))
    return

def Movimiento(Vacio_1, Vacio_2, direccion, tablero, opcion):
    if direccion == 1:
        if Vacio_1 - 1 == 1 or Vacio_1 - 1 == 0:
            Valor = tablero[Vacio_1 - 1][Vacio_2]
            tablero[Vacio_1 - 1][Vacio_2] = ""
            tablero[Vacio_1][Vacio_2] = Valor
            return True
        else:
            if opcion == 1:
                print("Movimiento no valido reintentar")
            return False
    elif direccion == 2:
        if Vacio_1 + 1 == 1 or Vacio_1 + 1 == 2:
            Valor = tablero[Vacio_1 + 1][Vacio_2]
            tablero[Vacio_1 + 1][Vacio_2] = ""
            tablero[Vacio_1][Vacio_2] = Valor
            return True
        else:
            if opcion == 1:
                print("Movimiento no valido reintentar")
            return False
    elif direccion == 3:
        if Vacio_2 + 1 == 1 or Vacio_2 + 1 == 2:
            Valor = tablero[Vacio_1][Vacio_2 + 1]
            tablero[Vacio_1][Vacio_2 + 1] = ""
            tablero[Vacio_1][Vacio_2] = Valor
            return True
        else:
            if opcion == 1:
                print("Movimiento no valido reintentar")
            return False
    elif direccion == 4:
        if Vacio_2 - 1 == 1 or Vacio_2 - 1 == 0:
            Valor = tablero[Vacio_1][Vacio_2 - 1]
            tablero[Vacio_1][Vacio_2 - 1] = ""
            tablero[Vacio_1][Vacio_2] = Valor
            return True
    elif direccion == 5:
        camino = resolver_ia(tablero)
        if camino:
            print("Solución encontrada! Movimientos realizados para resolver el tablero:")
            for i in range(len(camino)):
                Vacio_1, Vacio_2 = encontrar_vacio(tablero)
                Movimiento(Vacio_1, Vacio_2, camino[i], tablero, 1)
                if mostrar_tablero(tablero) != None:
                    print(mostrar_tablero(tablero))
                print(f" Solucion:{i + 1} ".center(50, "-"))
        else:
            print("EL tablero NO tiene solcion, por eso no podias XD")
    else:
        if opcion == 1:
            print("Movimiento no valido reintentar")
        return False

def verificar_ganador(tablero):
    objetivo = [[8, 7, 6], [5, 4, 3], [2, 1, ""]]
    return tablero == objetivo

def actualizar_matriz(tablero):
    while True:
        try:
            fila = int(input("Ingresa el número de fila:"))
            columna = int(input("Ingresa el número de columna:"))
            valor = input("Ingresa el valor de la casilla (1-8, deja en blanco para el espacio vacío): ")
            if valor == "":
                valor = ""
            else:
                valor = int(valor)
            if validar_movimiento(fila, columna, tablero, valor):
                tablero[fila][columna] = valor
                return
        except ValueError:
            print("Solo se permiten números. Intenta de nuevo.")
        print("Intenta de nuevo.")

def validar_movimiento(fila, columna, tablero, valor):
    if not (0 <= fila < 3) or not (0 <= columna < 3):
        print("Coordenadas fuera de los límites del tablero.")
        return False
    if tablero[fila][columna] != "":
        print("La celda ya está ocupada.")
        return False
    if not (valor == "" or 1 <= valor <= 8):
        print("Valor inválido. Debe ser un número entre 1 y 8 o un espacio vacío.")
        return False
    return True

def menu():
    opcion = input("Elige una opción:\n1) Random\n2) Llenar\n")
    if opcion == "1":
        tablero = crear_tablero()
        random.shuffle(tablero)
        for i in range(len(tablero)):
            random.shuffle(tablero[i])
    elif opcion == "2":
        tablero = crear_tablero_vacio()
        mostrar_tablero(tablero)
        for _ in range(9):
            actualizar_matriz(tablero)
            mostrar_tablero(tablero)
            time.sleep(1)
            os.system("cls")
        os.system("cls")
    else:
        print("Opción no válida")
        return
    while not verificar_ganador(tablero):
        mostrar_tablero(tablero)
        direccion = int(
            input("1) Arriba, 2) Abajo, 3) Derecha, 4) Izquierda, 5) Resolver IA \nDirección del movimiento: "))
        i_vacio, j_vacio = encontrar_vacio(tablero)
        Movimiento(i_vacio, j_vacio, direccion, tablero, 1)

    mostrar_tablero(tablero)
    print("\t--- GANADOR ---")

menu()
