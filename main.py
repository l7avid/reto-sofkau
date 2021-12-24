import sys
from utilidades import Utilidades
from jugador import Jugador
from presentador import Presentador

opcion=0
jugador = Jugador()
presentador = Presentador(jugador)


def listado_participantes():
    print("\nListado de Participantes\n")
    

def reglas_juego():
    print("\n *En este concurso el participante debe responder correctamente la mayor cantidad de preguntas posibles")
    print(" *El concurso consta de 5 rondas de preguntas, empezando por la categoría de menor nivel de dificultad")
    print(" *A medida que el concursante responda correctamente irá acumulando puntos y a su vez el nivel de dificultad aumentará")
    print(" *El participante puede decidir retirarse antes de responder cada pregunta y recibirá el acumulado parcial")
    print(" *Al responder correctamente la última pregunta se dará por finalizado el concurso y el participante habrá ganado")

def iniciar_juego():
    jugador.ingresar_nombre()
    presentador.presentacion()
    presentador.iniciar_concurso()
    #histParticipantes.append(objParticipante)

def main():

    while True:
        print("\n")
        print("|****************************|")
        print("|       Bienvenido  al       |")
        print("|          Concurso!!        |")
        print("|****************************|\n")
        print("Seleccione una de las siguientes opciones:\n");
        print("1. Reglamento del concurso")
        print("2. Iniciar")
        print("3. Ver historial de participantes")
        print("4. Salir")

        opcion = input("\nOpcion: ")
        opcion = Utilidades.es_numerico(opcion)

        if opcion == 1:
            reglas_juego()
        elif opcion == 2:
            iniciar_juego()
        elif opcion == 3:
            print(jugador.historial_juego())
        elif opcion == 4:
            sys.exit()
        else:
            print("Opcion no valida")

if __name__ == '__main__':
    main()