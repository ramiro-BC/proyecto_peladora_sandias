import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, \
      QGridLayout, QPushButton, QLabel,QVBoxLayout,QHBoxLayout,QDial, \
      QDoubleSpinBox,QSpinBox,QRadioButton
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QRunnable, QThreadPool, pyqtSignal as Signal, \
QObject, Qt
from temporizador import Temporizador
import time

class Caja(QLabel):#heredamos ventana
    def __init__ (self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")

class worker_signal(QObject): #entrega recados de lo que se debe modificar
    y1=Signal(bool)
    y2=Signal(bool)
    y3=Signal(bool)
    y4=Signal(bool)
    y5=Signal(bool)
    y6=Signal(bool)
    y7=Signal(bool)
    motor=Signal(bool)
    y8=Signal(bool)
    H_sube=Signal(bool)
    H_baja=Signal(bool)
    def __init__(self):
        super().__init__()

class Worker(QRunnable): #clase que modifica interfaz
    def __init__(self):
        super().__init__()
        self.signals=worker_signal()
    def prender_y1(self,estado:bool=False):
        try:
            self.signals.y1.emit(estado)
        except Exception as e:
            print("se obtuvo un error al emitir la señal")

    def prender_y2(self,estado:bool=False):
        try:
            self.signals.y2.emit(estado)
        except Exception as e:
            print("se obtuvo un error al emitir la señal")

    def prender_y3(self,estado:bool=False):
        try:
            self.signals.y3.emit(estado)
        except Exception as e:
            print("se obtuvo un error al emitir la señal")

    def prender_y4(self,estado:bool=False):
        try:
            self.signals.y4.emit(estado)
        except Exception as e:
            print("se obtuvo un error al emitir la señal")
    def prender_y5(self,estado:bool=False):
        try:
            self.signals.y5.emit(estado)
        except Exception as e:
            print("se obtuvo un error al emitir la señal")

    def prender_y6(self,estado:bool=False):
        try:
            self.signals.y6.emit(estado)
        except Exception as e:
            print("se obtuvo un error al emitir la señal")

    def prender_y7(self,estado:bool=False):
        try:
            self.signals.y7.emit(estado)
        except Exception as e:
            print("se obtuvo un error al emitir la señal")
    def prender_motor(self,estado:bool=False):
        try:
            self.signals.motor.emit(estado)
        except Exception as e:
            print("se obtuvo un error al emitir la señal")

    def prender_y8(self,estado:bool=False):
        try:
            self.signals.y8.emit(estado)
        except Exception as e:
            print("se obtuvo un error al emitir la señal")
    def prender_H_sube(self,estado:bool=False):
        try:
            self.signals.H_sube.emit(estado)
        except Exception as e:
            print("se obtuvo un error al emitir la señal")

    def prender_H_baja(self,estado:bool=False):
        try:
            self.signals.H_baja.emit(estado)
        except Exception as e:
            print("se obtuvo un error al emitir la señal")




class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MECANTRIX")
        self.resize(300,450)
        self.fuente=QFont("times new roman",18)

        self.TON_1_1=Temporizador("TON_00",3)
        self.TON_1_2=Temporizador("TON_01",1)

        # Crear el QTabWidget principal
        self.opciones = QTabWidget()
        self.setCentralWidget(self.opciones)
        # cambiamos el color de la pestana
        self.opciones.setStyleSheet("""QTabBar::tab:selected{background: #f2e40e;color:black;}""")

        

        # Crear la primera pestaña del QTabWidget principal
        self.MENU = QWidget()
        self.opciones.addTab(self.MENU, "MENU")

        # Crear un QTabWidget anidado dentro de la primera pestaña del QTabWidget principal
        self.MENU_OPCIONES = QTabWidget()
        self.layout_principal = QHBoxLayout()
        self.layout_principal.addWidget(self.MENU_OPCIONES)
        self.MENU.setLayout(self.layout_principal)

         
        # Crear la primera pestaña del QTabWidget anidado
        self.TIPO_DE_FRUTA = QWidget()
        self.MENU_OPCIONES.addTab(self.TIPO_DE_FRUTA, "TIPO DE FRUTA")

        # Crear un QGridLayout para la primera pestaña del QTabWidget anidado
        #self.VLAYOUT1 = QGridLayout()
        self.FRUTAS = QGridLayout()

        #fondo:
        self.fondoFrutas=Caja("#EDCD6C")
        self.FRUTAS.addWidget(self.fondoFrutas,0,0,4,5)

        # Agregar widgets al QGridLayout
        self.caja1=Caja("#D6030B")
        self.caja2=Caja("#FF4527")
        self.caja3=Caja("green")
        self.caja4=Caja("blue")

        self.layoutbotones=QVBoxLayout()

       

        self.label1 = QLabel("SELECCIONE EL TIPO DE FRUTA")
        self.label1.setFont(self.fuente)
        self.FRUTAS.addWidget(self.caja2,0,0,1,5) #esta caja parametriza
        self.FRUTAS.addWidget(self.label1,0,0,1,3)
        
        self.FRUTAS.addWidget(self.caja1,1,0,3,1)
        self.FRUTAS.addLayout(self.layoutbotones,1,0,3,1)
       
        self.button1 =QRadioButton("SANDIA")
        self.layoutbotones.addWidget(self.button1)  # Fila 0, Columna 1

        self.button2 =QRadioButton("PAPAYA")
        self.layoutbotones.addWidget(self.button2)  # Fila 1, Columna 0

        self.button3 =QRadioButton("MELON")
        self.layoutbotones.addWidget(self.button3)  # Fila 1, Columna 1

        self.button1.toggled.connect(self.estado_cambiado)
        self.button2.toggled.connect(self.estado_cambiado)
        self.button3.toggled.connect(self.estado_cambiado)
        


        self.FRUTAS.addWidget(self.caja4,4,0,1,5)
        self.buttonInicio = QPushButton("INICIAR")
        self.FRUTAS.addWidget(self.buttonInicio,4,0,1,1)
        self.buttonParo = QPushButton("DETENER")
        self.FRUTAS.addWidget(self.buttonParo,4,2,1,2)

        #cambir colores del boton
        
   


            # Crear una fuente personalizada
        fuente = QFont()
        fuente.setFamily("Palatino")
        fuente.setPointSize(15)
        fuente.setBold(True)

        # Aplicar la fuente al botón
        self.buttonParo.setFont(fuente)
        self.buttonInicio.setFont(fuente)

        self.buttonInicio.pressed.connect(lambda: self.cambiar_color_presionado(self.buttonInicio,"#12dd04"))
        self.buttonInicio.released.connect(lambda: self.cambiar_color_soltado(self.buttonInicio,"white"))
        self.buttonParo.pressed.connect(lambda: self.cambiar_color_presionado(self.buttonParo,"#fc2a00"))
        self.buttonParo.released.connect(lambda: self.cambiar_color_soltado(self.buttonParo,"white"))

        self.buttonInicio.pressed.connect(self.establcer_senal_arranque_high)
        self.buttonInicio.released.connect(self.establcer_senal_arranque_low)
        self.buttonParo.pressed.connect(self.establcer_senal_paro_high)
        self.buttonParo.released.connect(self.establcer_senal_paro_low)


         
        # Asignar el QGridLayout al widget de la pestaña anidada
        self.TIPO_DE_FRUTA.setLayout(self.FRUTAS)

        #///////////////////

           
        # Crear la SEGUNDA pestaña del QTabWidget anidado
        self.VER_ESTADO = QWidget()
        self.MENU_OPCIONES.addTab(self.VER_ESTADO, "VER ESTADO")

        # Crear otro VertyicalLayout para la segunda pestaña del QTabWidget anidado
        self.grid_layout2 = QGridLayout()
       ## self.grid_layout2_2 = QVBoxLayout()
        ##self.grid_layout2_3 = QVBoxLayout()

         # Crear otro HORIZONTALlLayout para la segunda pestaña del QTabWidget anidado
        self.H_layout2 = QHBoxLayout()
        self.H_layout2_2 = QHBoxLayout()
        self.H_layout2_3 = QHBoxLayout()

        ##asignar los horizontal a los vertical
        
        self.fondoEstado=Caja("#EDCD6C")

        self.grid_layout2.addWidget(self.fondoEstado,0,0,5,4)

        self.grid_layout2.addLayout(self.H_layout2,0,0)
        self.grid_layout2.addLayout(self.H_layout2_2,1,0)
          #inidcadores para los motores
        self.indorMotor=self.crear_indicador("black")
        self.etiquet_motor=QLabel("MOTOR FRUTA")
        self.etiquet_motor.setFont(self.fuente)
        self.indor_act_sube=self.crear_indicador("green")
        self.etiquet__act_sube=QLabel("SUBE HERRAMIENTA")
        self.etiquet__act_sube.setFont(self.fuente)
        self.indor_act_baja=self.crear_indicador("red")
        self.etiquet__act_baja=QLabel("BAJA HERRAMIENTA")
        self.etiquet__act_baja.setFont(self.fuente)
        
        self.grid_layout2.addWidget(self.etiquet_motor,2,0)
        self.grid_layout2.addWidget(self.indorMotor,2,2)
        self.grid_layout2.addWidget(self.etiquet__act_sube,3,0)
        self.grid_layout2.addWidget(self.indor_act_sube,3,2)
        self.grid_layout2.addWidget(self.etiquet__act_baja,4,0)
        self.grid_layout2.addWidget(self.indor_act_baja,4,2)
        


        # Agregar widgets al segundo H_Layout
        self.label2 = QLabel("TEMPERATURA:")
        self.H_layout2.addWidget(self.label2)

        self.numer_TEMP=QDoubleSpinBox()
        self.numer_TEMP.setPrefix("temp: ")#PREFUJO
        self.numer_TEMP.setSuffix( " °C")#sufijo
        self.numer_TEMP.setSingleStep (0.5)# aumenteo gradual
        self.numer_TEMP.setRange(-10, 10)
        self.numer_TEMP.valueChanged.connect(self.cambiar_valor)#imprimr rl valor al darle clic
        self.numer_TEMP.setFont(self.fuente)
    


        self.button4 = QPushButton("Botón 4")
        self.H_layout2.addWidget(self.numer_TEMP)  # Fila 0, Columna 1

        ##agregar widgete al layout H del 2do vertical

        self.num_FRUt = QLabel("NUMERO DE FRUTAS:")
        self.H_layout2_2.addWidget(self.num_FRUt) 

        self.contado2_frut = QSpinBox()
        self.contado2_frut.setSingleStep (1)# aumenteo gradual
        self.contado2_frut.setRange(-10, 10)
        self.contado2_frut.valueChanged.connect(self.cambiar_valor)
        
        self.H_layout2_2.addWidget(self.contado2_frut)  # Fila 1, Columna 1

       
        # Asignar el segundo QGridLayout al widget de la segunda pestaña anidada
        self.VER_ESTADO.setLayout(self.grid_layout2)

 #####################
        # Crear la SEGUNDA pestaña del QTabWidget principal
        self.CONFIG = QWidget()
        self.opciones.addTab(self.CONFIG, "CONFIGURACION")

        # Crear un QTabWidget anidado dentro de la SEGUNDAa pestaña del QTabWidget principal
        self.CONFIG_OPCIONES = QTabWidget()
        self.layoutCONF = QHBoxLayout()
        self.layoutCONF.addWidget(self.CONFIG_OPCIONES)
        self.CONFIG.setLayout(self.layoutCONF)

        #////////

         # Crear la primera pestaña del QTabWidget anidado DENTRO DE LA SEGUNDA
        self.VELOCIDAD_MOTOR = QWidget()
        self.CONFIG_OPCIONES.addTab(self.VELOCIDAD_MOTOR, "VELOCIDAD DEL MOTOR")

        #CREAR un QGridlayout para la pestaña

        self.vel_motor_layoutV2_1=QGridLayout()

        #agregamos widgets
        self.rpm=QLabel("Selecciona la velocidad")
        
        self.rpm.setFont(self.fuente)
        self.dial=QDial()
        self.dial.valueChanged.connect(self.valor_cambiado)
        self.dial.setRange(0,1750)
        
        self.fondoRPM=Caja("#EDCD6C")
        self.fondorpm=Caja("red")
        self.mvel_min=QLabel("MIN: 0 rpm")
        self.mvel_mmax=QLabel("MAX: 1750 rpm")
        self.vel_motor_layoutV2_1.addWidget(self.fondoRPM,0,0,4,4)

        self.vel_motor_layoutV2_1.addWidget(self.fondorpm,0,0,1,4)
        self.vel_motor_layoutV2_1.addWidget(self.rpm,0,0,1,4)
        self.vel_motor_layoutV2_1.addWidget(self.dial,1,1,2,2)
        self.vel_motor_layoutV2_1.addWidget(self.mvel_min,2,0,1,1)
        self.vel_motor_layoutV2_1.addWidget(self.mvel_mmax,2,3,1,1)

       

        #asignar ala qtab widget velocidad motor
        self.VELOCIDAD_MOTOR.setLayout(self.vel_motor_layoutV2_1)

        # Crear la SEGUNDA pestaña del QTabWidget anidado DENTRO DE LA SEGUNDA
        self.PROFUNDIDA_NABAJA = QWidget()
        self.CONFIG_OPCIONES.addTab(self.PROFUNDIDA_NABAJA, "PROFUNDIDAD DE NABAJA")
        

      

        ##############

         # Crear la tercera pestaña del QTabWidget principal
        self.incicador_sec = QWidget()
        self.opciones.addTab(self.incicador_sec, "ESTADO DE LA SECUENCIA")

       
        self.fondoEstadoSec=Caja("red")
        self.indicadorEstadoSec=Caja("blue")
        self.grid_layaut_inidic_sec=QGridLayout()
        #prton1
        self.layout_G_piston_1=QGridLayout()
        #piston2
        self.layout_G_piston_2=QGridLayout()
        #piston3
        self.layout_G_piston_3=QGridLayout()
        #piston4
        self.layout_G_piston_4=QGridLayout()
 
        self.incicador_sec.setLayout(self.grid_layaut_inidic_sec)
        self.grid_layaut_inidic_sec.addWidget(self.fondoEstadoSec,0,0,4,4)
        self.grid_layaut_inidic_sec.addLayout(self.layout_G_piston_1,0,0,1,4)
        self.grid_layaut_inidic_sec.addLayout(self.layout_G_piston_2,1,0,1,4)#fila 1 columna 0
        self.grid_layaut_inidic_sec.addLayout(self.layout_G_piston_3,2,0,1,4)#relatico al anterior
        self.grid_layaut_inidic_sec.addLayout(self.layout_G_piston_4,3,0,1,4)


        self.fondo_pis_1=self.crear_fondo("#ECF785")
        self.fondo_pis_2=self.crear_fondo("#FFBB15")
        self.fondo_pis_3=self.crear_fondo("#FFBB15")
        self.fondo_pis_4=self.crear_fondo("gray")

        #indicadores para las vaslvulas

        self.indorY1=self.crear_indicador("red")
        self.indorY2=self.crear_indicador("black")
        self.etiquet_piston1=QLabel("PISTON_1")
        self.etiquet_piston1.setFont(self.fuente)

        self.indorY3=self.crear_indicador("#2BD618")
        self.indorY4=self.crear_indicador("#40A9E3")
        self.etiquet_piston2=QLabel("PISTON_2")
        self.etiquet_piston2.setFont(self.fuente)

        self.indorY5=self.crear_indicador("#2BD618")
        self.indorY6=self.crear_indicador("#40A9E3")
        self.etiquet_piston3=QLabel("PISTON_3")
        self.etiquet_piston3.setFont(self.fuente)

        self.indorY7=self.crear_indicador("#0d0be8")
        self.indorY8=self.crear_indicador("#F71AD8")
        self.etiquet_piston4=QLabel("PISTON_4")
        self.etiquet_piston4.setFont(self.fuente)

        #agregamso los widgetes

        

        self.layout_G_piston_1.addWidget(self.fondo_pis_1,0,0,1,4)
        self.layout_G_piston_1.addWidget(self.etiquet_piston1,0,0,1,1)
        self.layout_G_piston_1.addWidget(self.indorY1,0,1,1,1)
        self.layout_G_piston_1.addWidget(self.indorY2,0,2,1,1)

        self.layout_G_piston_2.addWidget(self.fondo_pis_2,0,0,1,4)
        self.layout_G_piston_2.addWidget(self.etiquet_piston2,0,0,1,1)
        self.layout_G_piston_2.addWidget(self.indorY3,0,1,1,1)
        self.layout_G_piston_2.addWidget(self.indorY4,0,2,1,1)
        

        self.layout_G_piston_3.addWidget(self.fondo_pis_3,0,0,1,4)
        self.layout_G_piston_3.addWidget(self.etiquet_piston3,0,0,1,1)
        self.layout_G_piston_3.addWidget(self.indorY5,0,1,1,1)
        self.layout_G_piston_3.addWidget(self.indorY6,0,2,1,1)

        self.layout_G_piston_4.addWidget(self.fondo_pis_4,0,0,1,4)
        self.layout_G_piston_4.addWidget(self.etiquet_piston4,0,0,1,1)
        self.layout_G_piston_4.addWidget(self.indorY7,0,1,1,1)
        self.layout_G_piston_4.addWidget(self.indorY8,0,2,1,1)




        ################

        #cambiamos la posicion de widget
        self.MENU_OPCIONES.setTabPosition(QTabWidget.TabPosition.West)
        self.CONFIG_OPCIONES.setTabPosition(QTabWidget.TabPosition.West)

        #cambiamos interfaz enlazamos con elworker

        self.threadPool=QThreadPool()
        self.worker=Worker()
        self.worker.signals.y1.connect(self.cambiar_inicador_y1)
        self.worker.signals.y2.connect(self.cambiar_inicador_y2)
        self.worker.signals.y3.connect(self.cambiar_inicador_y3)
        self.worker.signals.y4.connect(self.cambiar_inidicador_y4)
        self.worker.signals.y5.connect(self.cambiar_inicador_y5)
        self.worker.signals.y6.connect(self.cambiar_inicador_y6)
        self.worker.signals.y7.connect(self.cambiar_inicador_y7)
        self.worker.signals.motor.connect(self.cambiar_inicador_motor)
        self.worker.signals.H_sube.connect(self.cambiar_inicador_H_sube)
        self.worker.signals.H_baja.connect(self.cambiar_inidicador_H_baja)
        self.worker.signals.y8.connect(self.cambiar_inidicador_y8)

    def cambiar_inicador_y1(self,estado:bool):
        if estado:
            self.modificar_indicador(self.indorY1,"red")
        else:
            self.modificar_indicador(self.indorY1,"white")
    
    def cambiar_inicador_y2(self,estado:bool):
        if estado:
            self.modificar_indicador(self.indorY2,"black")
        else:
            self.modificar_indicador(self.indorY2,"white")

    def cambiar_inicador_y3(self,estado:bool):
        if estado:
            self.modificar_indicador(self.indorY3,"#2BD618")
        else:
            self.modificar_indicador(self.indorY3,"white")

    def cambiar_inidicador_y4(self,estado:bool):
        if estado:
            self.modificar_indicador(self.indorY4,"#40A9E3")
        else:
            self.modificar_indicador(self.indorY4,"white")

    def cambiar_inicador_y5(self,estado:bool):
        if estado:
            self.modificar_indicador(self.indorY5,"#2BD618")
        else:
            self.modificar_indicador(self.indorY5,"white")
    
    def cambiar_inicador_y6(self,estado:bool):
        if estado:
            self.modificar_indicador(self.indorY6,"#40A9E3")
        else:
            self.modificar_indicador(self.indorY6,"white")

    def cambiar_inicador_y7(self,estado:bool):
        if estado:
            self.modificar_indicador(self.indorY7,"#0d0be8")
        else:
            self.modificar_indicador(self.indorY7,"white")

    def cambiar_inicador_motor(self,estado:bool):
        if estado:
            self.modificar_indicador(self.indorMotor,"#0d0be8")
        else:
            self.modificar_indicador(self.indorMotor,"white")

    def cambiar_inidicador_y8(self,estado:bool):
        if estado:
            self.modificar_indicador(self.indorY8,"#F71AD8")
        else:
            self.modificar_indicador(self.indorY8,"white")
    def cambiar_inicador_H_sube(self,estado:bool):
        if estado:
            self.modificar_indicador(self.indor_act_sube,"green")
        else:
            self.modificar_indicador(self.indor_act_sube,"white")

    def cambiar_inidicador_H_baja(self,estado:bool):
        if estado:
            self.modificar_indicador(self.indor_act_baja,"red")
        else:
            self.modificar_indicador(self.indor_act_baja,"white")



    def modificar_indicador (self,indicador,color):
        indicador.setStyleSheet(f"""
                    background-color: {color}; border-radius: 50""")
        
   
    def obtener_worker(self):
        return self.worker
   
   #########
    def valor_cambiado(self,valor):
        print(valor)

    def cambiar_valor (self, valor):
        print(valor)

  #3#####
    def crear_indicador(self, color:str="gray"):
         micajasera= QLabel()
         micajasera.setStyleSheet(f"""
                    background-color: {color}; border-radius: 50""")
         micajasera.setFixedSize(100,100)
         return micajasera
    
    def crear_fondo(self, color:str="gray"):
         mcajasera= QLabel()
         mcajasera.setStyleSheet(f"""
                    background-color: {color}; border-radius: 30""")
        ## mcajasera.setFixedSize(100,300)
         return mcajasera
    
    # estado de la los botnes radiales de las frutas

    def estado_cambiado(self,valor):
        boton:QRadioButton=self.sender()
        if boton.isChecked():
           print(valor,boton.text())

    #estado del botn de arranque y paro senales
    def establcer_senal_arranque_high(self,valor1=True):
            if self.semaforo:
             self.semaforo.cambiar_estado_memoria(3,valor1)
             #print(self.TON_1_1.salida)
             #print(f)
             #self.boton_paro.setCheckable(False)
             #print(valor1)
    def establcer_senal_arranque_low(self,valor1=False):
            if self.semaforo:
             self.semaforo.cambiar_estado_memoria(3,valor1)
             #print(self.TON_1_1.salida)
             #print(f)
             #self.boton_paro.setCheckable(False)
             #print(valor1)
    def establcer_senal_paro_high(self,valor=True):
            if self.semaforo:
             self.semaforo.cambiar_estado_memoria(4,valor)
             #print(self.TON_1_1.salida)
             #print(f)
             #self.boton_paro.setCheckable(False)
             #print(valor)
    def establcer_senal_paro_low(self,valor=False):
            if self.semaforo:
             self.semaforo.cambiar_estado_memoria(4,valor)
             #print(self.TON_1_1.salida)
             #print(f)
             #self.boton_paro.setCheckable(False)
             #print(valor)
    ####funciones pra cambiar el color de los bornes al presionarlos
    def cambiar_color_presionado(self,boton,color):
        boton.setStyleSheet(f"background-color: {color};")
    def cambiar_color_soltado(self,boton,color):
        boton.setStyleSheet(f"background-color: {color};")
    ######
    
    def establecer_semaforo (self,semaforo):
        self.semaforo=semaforo

def main():
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
if __name__ == "__main__":
    main()