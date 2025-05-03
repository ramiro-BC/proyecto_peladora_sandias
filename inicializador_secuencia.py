from PyQt6.QtWidgets import QApplication 
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtCore import Qt
import sys
from interfaz_peladora_frutas import Ventana #importamosinterfaz
from control_secuencia import Secunecia #importamos control
from electronica import Electronica
class Inicio (Ventana): #escribimos todo el codigo que queremos que se inicie
    def __init__(self):
        super().__init__()
         #se crea el control 
        semaforo = Secunecia() 
        #se pasa el semaforo a la interfaz
        self.establecer_semaforo(semaforo)
        semaforo.inuiciar()
        ##semaforo.establecer_worker()
        semaforo.establecer_worker(self.obtener_worker())
        
        #se crea electronica
        electronica=Electronica()
        #se pasa electronica al semaforo
        semaforo.establecer_electronica(electronica)

    
def main ():
    print("dentro de main")
    app = QApplication(sys.argv)
    ventana =Inicio()
    ventana.show()
    sys.exit(app.exec())

if __name__== "__main__":
    main()
    