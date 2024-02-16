"""
/*
 * Crea el juego conecta cuatro.
 *
 * Requisitos:
 * - Tablero de 7x6 (7 en el eje "x" y 6 en el "y").
 * - Fichas Rojas y Amarillas.
 * - No hay que implementar una funcionalidad que te permita jugar contra la App.
 *   Se asume que jugarán dos personas reales alternándose.
 * - Al seleccionar la columna se coloca la ficha en la parte inferior.
 * - Boton para reiniciar la partida en marcha
 * - Puedes añadirle todas las funcionalidades extra que consideres.
 */

"""
import sys
ganar = 0
filas = 6
columnas = 7
tablero = []
x = 0

#Declaramos los contadores en -1 para que en lugar de empezar en el primer digito, empiecen en el ultimo
contfila1 = -1
contfila2 = -1
contfila3 = -1
contfila4 = -1
contfila5 = -1
contfila6 = -1
contfila7 = -1
contadorganadoramarillo = 0
contadorganadorazul = 0
ganador =  0

def partida():
    #Inicializamos el tablero con None
    for inicializar in range(filas):
        tablero.append([None] * columnas)

        
        
    #Funcion que muestra el tabler
    def mostrar():
        for i in tablero:
            print(i)     
    print("El tablero al iniciar el juego es: ")
    mostrar()

    #Funcion para el turno azul
    def azul(): 
        global contfila1
        print("Turno azul:")
        azuly = int(input("Ingrese la coordenada x: ")) - 1
        #Comprobamos q  que el numero ingresado por el usuario esté dentro del rango
        if 0 <= azuly < filas + 1:
            #Si está dentro del rango ponemos el signo correspondiente
            if azuly  == 0: 
                if tablero[contfila1][0] is None:
                    tablero[contfila1][0] = 1
                    #Le restamos 1 al contador para que ahora vaya en la penultima y asi se va yendo
                    contfila1 -=1
            elif azuly == 1: 
                global contfila2
                if tablero[contfila2][1] is None:
                    tablero[contfila2][1] = 1
                    contfila2 -=1
            elif azuly == 2: 
                global contfila3
                if tablero[contfila3][2] is None:
                    tablero[contfila3][2] = 1
                    contfila3 -= 1
            elif azuly == 3: 
                global contfila4
                if tablero[contfila4][3] is None:
                    tablero[contfila4][3] = 1
                    contfila4 -= 1
            elif azuly == 4: 
                global contfila5
                if tablero[contfila5][4] is None:
                    tablero[contfila5][4] = 1
                    contfila5 -= 1
            elif azuly == 5: 
                global contfila6
                if tablero[contfila6][5] is None:
                    tablero[contfila6][5] = 1
                    contfila6 -= 1
            elif azuly == 6: 
                global contfila7
                if tablero[contfila7][6] is None:
                    tablero[contfila7][6] = 1
                    contfila7 -= 1
            #Por si el espacio que quiere ocupar ya está usandose
            else:
                print("Este espacio ya está en uso. Intente de nuevo.")
                azul()
        #Por si el numero que ingresa es mayor que el numero de filas
        else:
            print("Coordenada x fuera de los límites del tablero. Intente de nuevo.")
            azul()
        
    #Funcion para el turno amarillo 
    def amarillo(): 
        global contfila1
        print("Turno amarillo: ")
        
        amarilloy = int(input("Ingrese la coordenada x: ")) - 1
        #Comprobamos q  que el numero ingresado por el usuario esté dentro del rango

        if 0 <= amarilloy < filas + 1 and contfila1 != - 8:
            #Si está dentro del rango ponemos el signo correspondiente

            if amarilloy  == 0: 
                if tablero[contfila1][0] is None:
                    tablero[contfila1][0] = 2
                    #Le restamos 1 al contador para que ahora vaya en la penultima y asi se va yendo
                    contfila1 -=1
            elif amarilloy == 1: 
                global contfila2
                if tablero[contfila2][1] is None:
                    tablero[contfila2][1] = 2
                    contfila2 -=1
            elif amarilloy == 2: 
                global contfila3
                if tablero[contfila3][2] is None:
                    tablero[contfila3][2] = 2
                    contfila3 -= 1
            elif amarilloy == 3: 
                global contfila4
                if tablero[contfila4][3] is None:
                    tablero[contfila4][3] = 2
                    contfila4 -= 1
            elif amarilloy == 4: 
                global contfila5
                if tablero[contfila5][4] is None:
                    tablero[contfila5][4] = 2
                    contfila5 -= 1
            elif amarilloy == 5: 
                global contfila6
                if tablero[contfila6][5] is None:
                    tablero[contfila6][5] = 2
                    contfila6 -= 1
            elif amarilloy == 6: 
                global contfila7
                if tablero[contfila7][6] is None:
                    tablero[contfila7][6] = 2
                    contfila7 -= 1
            else:
                print("Este espacio ya está en uso. Intente de nuevo.")
                amarillo()
        else:
            print("Coordenada x fuera de los límites del tablero. Intente de nuevo.")
            amarillo()
    def ganador():
        global contadorganadorazul
        global contadorganadoramarillo
        global ganar
        
        for i in range(columnas):
            for j in range(filas -3):
                if tablero[j][i] == 1 and tablero[j + 1][i] == 1 and tablero[j + 2][i] == 1 and tablero[j + 3][i] == 1:
                    contadorganadorazul = 4
                    ganar = 1
                if tablero[j][i] == 2 and tablero[j + 1][i] == 2 and tablero[j + 2][i] == 2 and tablero[j + 3][i] == 2:
                    contadorganadoramarillo = 4
                    ganar = 1
        
        for i in range(filas):
            for j in range(columnas - 3):
                if tablero[i][j] == 1 and tablero[i][j + 1] == 1 and tablero[i][j + 2] == 1 and tablero[i][j + 3] == 1:
                    contadorganadorazul = 4
                    ganar = 1
                if tablero[i][j] == 2 and tablero[i][j + 1] == 2 and tablero[i][j + 2] == 2 and tablero[i][j + 3] == 2:
                    contadorganadoramarillo = 4
                    ganar = 1
                    
        # Verificar diagonales ascendentes
        for i in range(3, filas):
            for j in range(columnas - 3):
                if tablero[i][j] == 2 == tablero[i][j] == tablero[i - 1][j + 1] == tablero[i - 2][j + 2] == tablero[i - 3][j + 3] and tablero[i][j] != 0:
                    contadorganadoramarillo = 4
                    ganar = 1
                if tablero[i][j] == 1 == tablero[i][j] == tablero[i - 1][j + 1] == tablero[i - 2][j + 2] == tablero[i - 3][j + 3] and tablero[i][j] != 0:
                    contadorganadorazul = 4
                    ganar = 1    
        
        # Verificar diagonales descendentes
        for i in range(3, filas):
            for j in range(3, columnas):
                if tablero[i][j] == 2 == tablero[i - 1][j - 1] == tablero[i - 2][j - 2] == tablero[i - 3][j - 3] and tablero[i][j] != 0:
                    contadorganadoramarillo = 4
                    ganar = 1
                if tablero[i][j] == 1 == tablero[i - 1][j - 1] == tablero[i - 2][j - 2] == tablero[i - 3][j - 3] and tablero[i][j] != 0:
                    contadorganadorazul = 4
                    ganar = 1
                    
        if(contadorganadoramarillo == 4 and contadorganadorazul < 4):
            print("EL ganador es el amarillo. ¡Felicidades!")
        elif(contadorganadoramarillo < 4 and contadorganadorazul == 4):
            print("El ganador es el azul. ¡Felicidades!")

    while ganar != 1:
        amarillo()
        mostrar()
        ganador()

        if ganar != 1:
            azul()
            mostrar()
            ganador()


partida()