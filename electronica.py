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
        self.DO_03=5
        self.DO_04=6
        self.DO_05=13
        self.DO_06=19
        self.DO_07=26
        self.DO_08=16
        self.DO_09=20
        #entrads
        self.x=[]
        for i in range (10):
            self.x.append(False)
        #salidas
        self.y=[]
        for i in range (20):
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
                self.DO_03:gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE ),
                self.DO_04:gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE ),
                self.DO_05:gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE ),
                self.DO_06:gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE ),
                self.DO_07:gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE ),
                self.DO_08:gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE ),
                self.DO_09:gpiod.Linesettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE ),
            }
        )
    def iniciar(self):
        self.funcionado_pines=True
        while self.funcionado_pines:
            #mapeo de variables

            self.x[0]=True if self.request.get_value(self.DI_00)==Value.ACTIVE else False
            self.x[2]=True if self.request.get_value(self.DI_01)==Value.ACTIVE else False
            
            self.request.set_value(self.DO_00,Value.ACTIVE if self.y[3]==True else Value.INACTIVE)
            self.request.set_value(self.DO_01,Value.ACTIVE if self.y[5]==True else Value.INACTIVE)
            self.request.set_value(self.DO_02,Value.ACTIVE if self.y[1]==True else Value.INACTIVE)
            self.request.set_value(self.DO_03,Value.ACTIVE if self.y[7]==True else Value.INACTIVE)
            self.request.set_value(self.DO_04,Value.ACTIVE if self.y[4]==True else Value.INACTIVE)
            self.request.set_value(self.DO_05,Value.ACTIVE if self.y[6]==True else Value.INACTIVE)
            self.request.set_value(self.DO_06,Value.ACTIVE if self.y[2]==True else Value.INACTIVE)
            self.request.set_value(self.DO_07,Value.ACTIVE if self.y[8]==True else Value.INACTIVE)

            #Motor
            self.request.set_value(self.DO_08,Value.ACTIVE if self.y[9]==True else Value.INACTIVE)
        

            time.sleep(0.01)
        


        
def main():
    electronica=Electronica()
    #electronica.iniciar
    
if __name__=="__main__":
    main()