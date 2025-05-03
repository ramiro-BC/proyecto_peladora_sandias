import time
import gpiod
from gpiod.line  import Direction, Value
import threading

class Electronica():
    def __init__(self):
        super().__init__()
        print("dentro de la clase electronica")
        self.DI_00=14
        self.DI_01=15

        self.DO_00=17
        self.DO_01=27
        self.DO_02=22
        #entrads
        self.x=[]
        for i in range (10):
            self.x.append(False)
        #salidas
        self.y=[]
        for i in range (10):
            self.y.append(False)
        #memorias
        self.M=[]
        for i in range (10):
            self.M.append(False)

        self.funcionado_pines=False

        self.configurar_pines()

        self.tarea=threading.Thread(target= self.iniciar)
        self.tarea.start()
    
        

    def configurar_pines(self):
        self.chip=gpiod.Chip("/dev/gpiochip0") #ubicaacion de memoria opara cceder alos pines de raspberry
        self.request=self.chip.request_lines(
            consumer="prueba led",
            config={
                #ENTRADA
                self.DI_00:gpiod.LineSettings(direction=Direction.INPUT),
                self.DI_01:gpiod.LineSettings(direction=Direction.INPUT),
                #SALIDA DIGITAL
                self.DO_00:gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE ),
                self.DO_01:gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE ),
                self.DO_02:gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE ),
            }
        )
    def iniciar(self):
        self.funcionado_pines=True
        while self.funcionado_pines:
            #mapeo de variables

            self.x[0]=True if self.request.get_value(self.DI_00)==Value.ACTIVE else False
            self.x[2]=True if self.request.get_value(self.DI_01)==Value.ACTIVE else False
            
            self.request.set_value(self.DO_00,Value.ACTIVE if self.y[3]==True else Value.INACTIVE)
            self.request.set_value(self.DO_01,Value.ACTIVE if self.y[2]==True else Value.INACTIVE)
            self.request.set_value(self.DO_02,Value.ACTIVE if self.y[1]==True else Value.INACTIVE)
            time.sleep(0.01)
        


        
def main():
    electronica=Electronica()
    #electronica.iniciar
    
if __name__=="__main__":
    main()