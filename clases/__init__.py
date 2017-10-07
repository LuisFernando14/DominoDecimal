import random

if __name__ == '__main__':
    print "Hola"
    fichasJugador1 = []
    fichasJugador2 = []
    tablero = [] # En teoría solo acepta unas 4 posiciones y no será una lista de listas
    puntajeJugador1 = 0;
    puntajeJugador2 = 0;
    condicion = True
    movimeintoJugador = True

    fichas = [
        [0,0], [0,1], [0,2], [0,3], [0,4], [0,5], [0,6],
        [1,1], [1,2], [1,3], [1,4], [1,5], [1,6], [2,2],
        [2,3], [2,4], [2,5], [2,6], [3,3], [3,4], [3,5],
        [3,6], [4,4], [4,5], [4,6], [5,5], [5,6], [6,6]
    ]

    for ficha in fichas:
        ficha[1]+=1
        # print ficha[1]

    def repartirFichas (fichas, jugador):
        for i in range (5):
            posicion = random.randrange(0, len(fichas), 1)
            if jugador.__contains__(fichas[posicion]):
                i-=1
                continue
            jugador.append(fichas[posicion])
            fichas.remove(fichas[posicion])
    repartirFichas(fichas, fichasJugador1)
    repartirFichas(fichas, fichasJugador2)

    print "Fichas del jugador 1"
    for ficha in fichasJugador1:
        print ficha
    print "Fichas del jugador 2"
    for ficha in fichasJugador2:
        print ficha
    print "Fichas en la banca"
    for ficha in fichas:
        print ficha
    #Siempre será el jugador uno el que comienza
    if(fichasJugador1.__contains__([5,5])): #empieza el jugador uno
        tablero.append([5,5])
        fichasJugador1.remove([5,5])
        tablero.append([5,5])
        movimeintoJugador = False
    elif (fichasJugador2.__contains__([5,5])):
        tablero.append([5, 5])
        fichasJugador2.remove([5, 5])
        tablero.append([5, 5])
    #Aquí ya empieza el juego al cien
    while (len(fichasJugador1) != 0 and len(fichasJugador2) != 0) or condicion:
        if(movimeintoJugador): #jugador 1
            #Verificar si puede hacer un movimiento
            #verificar si puede tomar de la sobra
            # Buscar fichas en la banca (los extremos) para ver cuál podemos poner
            # poner la ficha
            #No hacer nada y ceder el movimiento
            pass
        else: #jugador 2
            pass
        pass