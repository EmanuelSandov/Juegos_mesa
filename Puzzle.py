import random

tablero = [[8, 7, 6],
           [5, 4, 3],
           [2, 1, ""]]

random.shuffle(tablero)


def Tablero():
    print("|", tablero[0][0], "|", tablero[0][1], "|", tablero[0][2], "|")
    print("|", tablero[1][0], "|", tablero[1][1], "|", tablero[1][2], "|")
    print("|", tablero[2][0], "|", tablero[2][1], "|", tablero[2][2], "|")


#Buscar vacio
def Vacio(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if tablero[i][j] == "":
                return i, j


def Movimiento(Vacio_1, Vacio_2, direccion, tablero):
    if direccion == 1:
        if Vacio_1 - 1 == 1 or Vacio_1 - 1 == 0:
            Valor = tablero[Vacio_1 - 1][Vacio_2]
            tablero[Vacio_1 - 1][Vacio_2] = ""
            tablero[Vacio_1][Vacio_2] = Valor
        else:
            print("Movimiento no valido reintentar")
    elif direccion == 2:
        if Vacio_1 + 1 == 1 or Vacio_1 + 1 == 2:
            Valor = tablero[Vacio_1 + 1][Vacio_2]
            tablero[Vacio_1 + 1][Vacio_2] = ""
            tablero[Vacio_1][Vacio_2] = Valor
        else:
            print("Movimiento no valido reintentar")
    elif direccion == 3:
        if Vacio_2 + 1 == 1 or Vacio_2 + 1 == 2:
            Valor = tablero[Vacio_1][Vacio_2 + 1]
            tablero[Vacio_1][Vacio_2 + 1] = ""
            tablero[Vacio_1][Vacio_2] = Valor
        else:
            print("Movimiento no valido reintentar")
    elif direccion == 4:
        if Vacio_2 - 1 == 1 or Vacio_2 - 1 == 0:
            Valor = tablero[Vacio_1][Vacio_2 - 1]
            tablero[Vacio_1][Vacio_2 - 1] = ""
            tablero[Vacio_1][Vacio_2] = Valor
        else:
            print("Movimiento no valido reintentar")


def Verificar(tablero):
    Valor = 8
    Fin = 0
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if tablero[i][j] == Valor:
                Valor -= 1
                if Valor == 0:
                    Fin = 1
    return Fin


Fin = 0
while (Fin == 0):
    print("1)Arriba, 2)Abajo, 3)Derecha, 4)Izquierda")
    Tablero()
    direccion = int(input("Direccion del movimiento:"))
    Vacio_1, Vacio_2 = Vacio(tablero)
    Movimiento(Vacio_1, Vacio_2, direccion, tablero)
    Fin = Verificar(tablero)
    Tablero()
print("GANADOR")
