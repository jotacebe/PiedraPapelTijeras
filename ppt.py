import random as rn
from os import system as sm

opciones = ["Piedra", "Papel", "Tijeras"]

def inicio_partida():
    ronda_actual = 0
    puntos_jugador = 0
    puntos_ordenador = 0
    sm("cls")
    print("JUEGO DE PIEDRA, PAPEL Y TIJERAS\n")
    print("Reglas del juego:\n")
    print("En cada ronda podrás elegir sacar entre Piedra, Papel o Tijeras.")
    print("El ordenador sacará aleatoriamente alguna de esas opciones.")
    print("Quien gana la ronda se determina por las siguientes reglas:")
    print("\tPapel gana a Piedra")
    print("\tPiedra gana a Tijeras")
    print("\tTijeras gana a Papel\n")
    print("Gana la partida el jugador que más rondas haya ganado en total.\n")
    nombre_jugador = input("Escribe tu nombre: ")
    nombre_jugador = "Jugador" if nombre_jugador == "" else nombre_jugador
    while True:
        try:
            rondas = int(input(f"{nombre_jugador}, elige el número de rondas que quieres jugar: "))
            print()
            break    
        except:
            print("Debes de introducir un valor numérico.")
    jugadas(rondas, ronda_actual,nombre_jugador, puntos_jugador, puntos_ordenador)

def jugadas(rondas, ronda_actual,nombre_jugador, puntos_jugador, puntos_ordenador):
    while ronda_actual < rondas:
        ronda_actual += 1
        print(f"Ronda {ronda_actual}")
        tirada_jugador = jugada_jugador(nombre_jugador)
        tirada_ordenador = rn.choice(opciones)
        print(f"La tirada del ordenador ha sido {tirada_ordenador}")
        ganador = validar(tirada_jugador, tirada_ordenador)
        if ganador != 0:
            puntos_jugador += 1 if ganador == tirada_jugador else 0
            puntos_ordenador +=1 if ganador == tirada_ordenador else 0
        print(f"\n{tirada_jugador} vs {tirada_ordenador}", end=" ")
        print(f"→ Gana {ganador}") if ganador == tirada_jugador or ganador == tirada_ordenador else print("→ La tirada es empate.")
        print(f"Ronda {ronda_actual}: {nombre_jugador} {puntos_jugador} - Ordenador {puntos_ordenador}\n")
    resultado_final(rondas,nombre_jugador, puntos_jugador, puntos_ordenador)

def jugada_jugador(nombre_jugador):
    tirada_jugador = ""
    while tirada_jugador not in opciones:
        tirada_jugador = input(f"{nombre_jugador}, haz tu tirada: ").capitalize()
    return tirada_jugador

def validar(tirada_jugador, tirada_ordenador):
    ganador = 0
    if tirada_jugador == "Piedra":
        if tirada_ordenador == "Papel":
            ganador = tirada_ordenador
        elif tirada_ordenador == "Tijeras":
            ganador = tirada_jugador
    elif tirada_jugador == "Papel":
        if tirada_ordenador == "Piedra":
            ganador = tirada_jugador
        elif tirada_ordenador == "Tijeras":
            ganador = tirada_ordenador
    elif tirada_jugador == "Tijeras":
        if tirada_ordenador == "Piedra":
            ganador = tirada_ordenador
        elif tirada_ordenador == "Papel":
            ganador = tirada_jugador
    return ganador

def resultado_final(rondas,nombre_jugador, puntos_jugador, puntos_ordenador):
    nueva = ""
    print("MARCADOR FINAL\n")
    print(f"Se han jugado {rondas} rondas con el resultado de:")
    print(f"\t{nombre_jugador}: {puntos_jugador} rondas ganadas.")
    print(f"\tOrdenador: {puntos_ordenador} rondas ganadas.")
    print(f"\t{rondas - puntos_jugador - puntos_ordenador} rondas han terminado en empate.\n")
    if puntos_jugador > puntos_ordenador:
        print(f"El ganador de la partida ha sido {nombre_jugador}.")
    elif puntos_ordenador > puntos_jugador:
        print(f"El ganador de la partida ha sido el ordenador.")
    else:
        print("La partida ha terminado en empate.")
    print()
    while nueva not in ["s","n"]:
        nueva = input("¿Quieres jugar otra partida? (s/n) ").lower()
    if nueva == "s":
        inicio_partida()
    else:
        sm("cls")
        sm("exit")

if __name__ == "__main__":
    inicio_partida()