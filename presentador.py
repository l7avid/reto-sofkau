from banco_preguntas import BancoPreguntas
from jugador import Jugador
import sys
from utilidades import Utilidades

premio_inicial = 500000
histParticipantes=[]

class Presentador:
    
    def __init__(self,jugador) -> None:
        self.jugador = jugador

    def presentacion(self) -> None:
        #objParticipante = Jugador(self.nombre,0)
        print("Bienvenido " + self.jugador.nombre + " - Premio: 0 pesos")
        #histParticipantes.append(objParticipante)
        #return histParticipantes

    
    def iniciar_concurso(self) -> None:
        acumulado=0
        #print("Primera pregunta por: ${}".format(premio_inicial))
        for ronda in range(1,6):
            self.jugador.ronda = ronda
            premio=premio_inicial*ronda
            if ronda>1:
                retiro=input("Desea continuar? 1.Si  2.No\n")
                retiro = Utilidades.es_numerico(retiro)
                if retiro == 1:
                    pass
                else:
                    print("Ha ganado ${}".format(acumulado))
                    #self.jugador.guardar_registro()
                    break
                    #sys.exit()
                     
            print("Pregunta por: ${}".format(premio))
            banco_preguntas = BancoPreguntas()
            pregunta = banco_preguntas.seleccionar_pregunta(ronda)
            print(pregunta.sentencia)
            print("a. "+pregunta.opciones[0])
            print("b. "+pregunta.opciones[1])
            print("c. "+pregunta.opciones[2])
            print("d. "+pregunta.opciones[3])
            self.respuesta_participante=input("Ingrese su respuesta: ")
            if pregunta.respuesta[0] == self.respuesta_participante:
                print("Correcto!")
                acumulado=acumulado+premio
                self.jugador.puntaje = acumulado
                if ronda==5:
                    print("FELIIDADES! HA GANADO EL CONCURSO\n")
                    print("Premio total: ", acumulado)
                else:
                    print("Su acumulado hasta el momento es de: ",acumulado)
            else:
                print("Has perdido :c Gracias por participar!")
                break
        self.jugador.guardar_registro()    