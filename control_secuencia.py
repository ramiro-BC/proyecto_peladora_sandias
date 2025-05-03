import threading
import time
from temporizador import Temporizador
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtCore import QRunnable, QThreadPool, pyqtSignal as Signal, \
QObject, Qt


class Secunecia():
    def __init__(self):
        print("dentro de semaforo")

        self.TON_0=Temporizador("TON_00",2)
        self.TON_1=Temporizador("TON_01",3)
        self.TON_2=Temporizador("TON_01",3)
        self.TON_3=Temporizador("TON_01",3)
        self.TON_4=Temporizador("TON_02",3)

        self.TON_5=Temporizador("TON_03",3)
        
        self.TON_6=Temporizador("TON_04",9)
        self.TON_6_1=Temporizador("TON_041",1)#RETARDO DE ACTIVACION DE LA NABAJA
        self.TON_6_2=Temporizador("TON_042",4)
        self.TON_6_3=Temporizador("TON_043",4)
        self.TON_7=Temporizador("TON_03",2)
        self.TON_8=Temporizador("TON_04",3)
        self.TON_9=Temporizador("TON_03",3)
        self.TON_10=Temporizador("TON_04",1)

        self.M=[] #lisat de m´s pra mmapear
        for i in range(20):
            self.M.append(False)

        self.M[2]=False
        
        self.finish=1
        self.M0=False
        self.M1=True
        self.aux1=False
        self.aux2=False
        self.y1=False
        self.y2=False
        self.y3=False
        self.y4=False
        self.y5=False
        self.y6=False
        self.y7=False
        self.motor=False
        self.y8=False
        self.y9=False
        self.in1=False
        self.in2=False
        ##worker pra enlace
        self.worker=None
        self.electronica=None

        self.tarea=threading.Thread(target= self.secuencia_funcionando)

    def inuiciar(self):
        if self.tarea:
            self.tarea.start() 


    def secuencia_funcionando(self):
        while  True:
           #ks print("el se mafor esta funcionando")
            self.M0=(self.M[0] or self.M0 or self.M[3]) and not self.TON_8.salida and not self.M[1] and not self.M[4]
            self.TON_0.entrada=self.M0 and not self.TON_8.salida
            self.TON_0.actualizar()
            self.TON_1.entrada=self.M0 and self.TON_0.salida
            self.TON_1.actualizar()
            self.TON_2.entrada=self.M0 and self.TON_1.salida
            self.TON_2.actualizar()
            self.TON_3.entrada=self.M0 and self.TON_2.salida
            self.TON_3.actualizar()
            self.TON_4.entrada=self.M0 and self.TON_3.salida
            self.TON_4.actualizar()
            self.TON_5.entrada=self.M0 and self.TON_4.salida
            self.TON_5.actualizar()
            self.TON_6.entrada=self.M0 and self.TON_5.salida
            self.TON_6.actualizar()
            self.TON_6_1.entrada=self.M0 and self.TON_5.salida
            self.TON_6_1.actualizar()
            self.TON_6_2.entrada=self.M0 and self.TON_6_1.salida
            self.TON_6_2.actualizar()
            self.TON_6_3.entrada=self.M0 and self.TON_6_2.salida
            self.TON_6_3.actualizar()
            self.TON_7.entrada=self.M0 and self.TON_6.salida
            self.TON_7.actualizar()
            self.TON_8.entrada=self.M0 and self.TON_7.salida
            self.TON_8.actualizar()
            #self.TON_9.entrada=self.M0 and self.TON_7.salida
            #self.TON_8.actualizar()




            self.y3=self.TON_0.salida and not self.TON_3.salida
            self.y5=self.TON_0.salida and not self.TON_3.salida
            self.y1=self.TON_1.salida and not self.TON_4.salida
            self.y7=self.TON_2.salida and not self.TON_7.salida
            self.y4=self.TON_3.salida 
            self.y6=self.TON_3.salida 
            self.y2=self.TON_4.salida
            self.motor=self.TON_5.salida and not self.TON_6.salida
            self.in1=self.TON_6_1.salida and not self.TON_6_2.salida
            self.in2=self.TON_6_2.salida and not self.TON_6_3.salida
            self.y8=self.TON_7.salida




            print(f"""Y1: {self.y1} Y2: {self.y2} Y3: {self.y3} Y4: {self.y4} Y5: {self.y5} \
                  
             Y6: {self.y6} Y7:{self.y7} Y8:{self.y8} MOTOR:{self.motor}""")
            #mapeando haci la interfaz
            if self.worker:
                self.worker.prender_y3(self.y3)
                self.worker.prender_y5(self.y5)
                self.worker.prender_y1(self.y1)
                self.worker.prender_y7(self.y7)
                self.worker.prender_y4(self.y4)
                self.worker.prender_y6(self.y6)
                self.worker.prender_y2(self.y2)
                self.worker.prender_motor(self.motor)
                self.worker.prender_H_sube(self.in1)
                self.worker.prender_H_baja(self.in2)
                self.worker.prender_y8(self.y8)
            """if self.worker:
                self.worker.prender_luz_verde(self.luzverde)
            if self.worker:
                self.worker.prender_luz_azul(self.luzazul)"""
             #enlazamos hacia la electronica
            if self.electronica:
                self.electronica.y[1]=self.y1
                self.electronica.y[2]=self.y2
                #el valor almacenado en  self.motor se ira al pinaperado de la raspberry en y[3] m
                self.electronica.y[3]=self.motor 

                # enlazar botones fisicos
                #el valor que entre en el mapeo del pin de la raspbery se almacena en 
                #la memoria m[0]
                self.M[0]= self.electronica.x[0]
                 #el valor que entre en el mapeo en [x2] del pin de la raspbery se almacena en 
                #la memoria m[1]
                self.M[1]= self.electronica.x[2] 
            
            
            time.sleep(0.01)
     #cambamos el estado de la memoria
    def cambiar_estado_memoria(self,numero,estado):
        if numero < len(self.M) and numero >= 0:
            self.M[numero]=estado

    def establecer_worker(self, worker):
        self.worker=worker
    
    def establecer_electronica (self,electronica):
        self.electronica = electronica
    
    def obtener_semaforo(self):
        return self
    
def main():
    print("dentro de Main")
    secuencia=Secunecia()
    secuencia.inuiciar()

if __name__=="__main__":
    main()