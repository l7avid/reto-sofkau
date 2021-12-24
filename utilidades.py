import sys
import time

class Utilidades:

    @staticmethod
    def es_numerico(retiro):
        try:
            int(retiro)
            retiro = int(retiro)
            return retiro
        except ValueError:
            print ("Opcion no valida")
            time.sleep(1)
            print("Gracias por participar...")
            #sys.exit()
            
