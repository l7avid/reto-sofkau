import csv
from datetime import datetime
import pandas as pd
from utilidades import Utilidades

class Jugador:

    def __init__(self,nombre='',puntaje=0,ronda=0) -> None: 
        self.nombre = nombre
        self.puntaje = puntaje
        self.ronda = ronda
    
    def ingresar_nombre(self):
        self.nombre=input("Ingrese su nombre: ")
    
    def entregar_datos(self):
        print("Nombre: {} - Puntaje: {}".format(self.nombre, self.puntaje))

    def guardar_registro(self):
        with open('Historial.csv','a+',encoding='UTF8',newline='') as historial: 
            writer = csv.writer(historial)
            # write the header
            writer.writerow([datetime.now(), self.nombre, self.puntaje, self.ronda])
        pass

    def historial_juego(self):

        #historial_jugador=pd.read_csv("Historial.csv", sep=',')
        historial_general=pd.read_csv("Historial.csv", sep=',')
        ver_historial_gral = input("Desea ver el historial general? 1.Si  2.No\n")
        ver_historial_gral = Utilidades.es_numerico(ver_historial_gral)

        if ver_historial_gral == 1:
            return historial_general.tail()
        
        else:
            if self.nombre:
                historial_jugador=historial_general[historial_general["Nombre"]==self.nombre]

            if historial_jugador.empty:
                return "El jugador no tiene registros"

            return historial_jugador.tail()
        

