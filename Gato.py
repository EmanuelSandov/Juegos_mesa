from random import randrange

Tablero = [["_", "_", "_"],
           ["_", "_", "_"],
           ["_", "_", "_"]]
Ganador = False

print("JUEGO DEL GATO")
print("1) 1 vs 1")
print("2) 1 vs IA")
X = int(input("Selecciona con quien quiere jugar:  "))

if X == 1:
    for i in range(0, 9):
        for j in range(0, 2):
            if Tablero[0][j] == 'X' and Tablero[1][j] == 'X' and Tablero[2][j] == 'X':
                print("Ganador el jugador 1")
                exit()
            elif Tablero[j][0] == 'X' and Tablero[j][1] == 'X' and Tablero[j][2] == 'X':
                print("Ganador el jugador 1")
                exit()
            elif Tablero[0][0] == 'X' and Tablero[1][1] == 'X' and Tablero[2][2] == 'X':
                print("Ganador el jugador 1")
                exit()
            elif Tablero[0][2] == 'X' and Tablero[1][1] == 'X' and Tablero[2][0] == 'X':
                print("Ganador el jugador 1")
                exit()
            elif Tablero[0][0] == 'Y' and Tablero[1][1] == 'Y' and Tablero[2][2] == 'Y':
                print("Ganador el jugador 2")
                exit()
            elif Tablero[0][2] == 'Y' and Tablero[1][1] == 'Y' and Tablero[2][0] == 'Y':
                print("Ganador el jugador 2")
                exit()
            elif Tablero[0][j] == 'Y' and Tablero[1][j] == 'Y' and Tablero[2][j] == 'Y':
                print("Ganador el jugador 2")
                exit()
            elif Tablero[j][0] == 'Y' and Tablero[j][1] == 'Y' and Tablero[j][2] == 'Y':
                print("Ganador el jugador 2")
                exit()

        if i % 2 == 0:
            ValidoX = 1
            ValidoY = 1
            while ValidoX == 1:
                TiroX_Fila = int(input("Ingrese la fila para tirar X: "))
                TiroX_Colum = int(input("Ingrese la columna para tirar X: "))
                if Tablero[TiroX_Fila][TiroX_Colum] == ("X") or Tablero[TiroX_Fila][TiroX_Colum] == ("Y"):
                    print("El tiro no valido reintentar ")
                else:
                    Tablero[TiroX_Fila][TiroX_Colum] = ("X")
                    print("____________________________________")
                    print(Tablero[0][0], Tablero[0][1], Tablero[0][2])
                    print(Tablero[1][0], Tablero[1][1], Tablero[1][2])
                    print(Tablero[2][0], Tablero[2][1], Tablero[2][2])
                    print("____________________________________")
                    ValidoX = 0
        else:
            while ValidoY == 1:
                TiroY_Fila = int(input("Ingrese la fila para tirar Y: "))
                TiroY_Colum = int(input("Ingrese la columna para tirar Y: "))
                if Tablero[TiroY_Fila][TiroY_Colum] == ("X") or Tablero[TiroY_Fila][TiroY_Colum] == ("Y"):
                    print("El tiro no valido reintentar \n")
                else:
                    Tablero[TiroY_Fila][TiroY_Colum] = ("Y")
                    print("____________________________________")
                    print(Tablero[0][0], Tablero[0][1], Tablero[0][2])
                    print(Tablero[1][0], Tablero[1][1], Tablero[1][2])
                    print(Tablero[2][0], Tablero[2][1], Tablero[2][2])
                    print("____________________________________")
                    ValidoY = 0
    print("Tablero lleno ")
elif X == 2:
    for i in range(0, 9):
        for j in range(0, 2):
            if Tablero[0][j] == 'X' and Tablero[1][j] == 'X' and Tablero[2][j] == 'X':
                print("Ganaste")
                exit()
            elif Tablero[j][0] == 'X' and Tablero[j][1] == 'X' and Tablero[j][2] == 'X':
                print("Ganaste")
                exit()
            elif Tablero[0][0] == 'X' and Tablero[1][1] == 'X' and Tablero[2][2] == 'X':
                print("Ganaste")
                exit()
            elif Tablero[0][2] == 'X' and Tablero[1][1] == 'X' and Tablero[2][0] == 'X':
                print("Ganaste")
                exit()
            elif Tablero[0][0] == 'Y' and Tablero[1][1] == 'Y' and Tablero[2][2] == 'Y':
                print("Ganador IA ")
                exit()
            elif Tablero[0][2] == 'Y' and Tablero[1][1] == 'Y' and Tablero[2][0] == 'Y':
                print("Ganador IA ")
                exit()
            elif Tablero[0][j] == 'Y' and Tablero[1][j] == 'Y' and Tablero[2][j] == 'Y':
                print("Ganador IA ")
                exit()
            elif Tablero[j][0] == 'Y' and Tablero[j][1] == 'Y' and Tablero[j][2] == 'Y':
                print("Ganador IA ")
                exit()

        if i % 2 == 0:
            ValidoX = 1
            ValidoY = 1
            while ValidoX == 1:
                TiroX_Fila = int(input("Ingrese la fila para tirar X: "))
                TiroX_Colum = int(input("Ingrese la columna para tirar X: "))
                if Tablero[TiroX_Fila][TiroX_Colum] == ("X") or Tablero[TiroX_Fila][TiroX_Colum] == ("Y"):
                    print("El tiro no valido reintentar ")
                else:
                    Tablero[TiroX_Fila][TiroX_Colum] = ("X")
                    print("____________________________________")
                    print(Tablero[0][0], Tablero[0][1], Tablero[0][2])
                    print(Tablero[1][0], Tablero[1][1], Tablero[1][2])
                    print(Tablero[2][0], Tablero[2][1], Tablero[2][2])
                    print("____________________________________")
                    ValidoX = 0
        else:
            while ValidoY == 1:
                TiroY_Fila = randrange(3)
                TiroY_Colum = randrange(3)
                if Tablero[TiroY_Fila][TiroY_Colum] == ("X") or Tablero[TiroY_Fila][TiroY_Colum] == ("Y"):
                    print("El tiro no valido reintentar IA\n")
                else:
                    Tablero[TiroY_Fila][TiroY_Colum] = ("Y")
                    print("____________________________________")
                    print(Tablero[0][0], Tablero[0][1], Tablero[0][2])
                    print(Tablero[1][0], Tablero[1][1], Tablero[1][2])
                    print(Tablero[2][0], Tablero[2][1], Tablero[2][2])
                    print("____________________________________")
                    ValidoY = 0
    print("Tablero lleno ")