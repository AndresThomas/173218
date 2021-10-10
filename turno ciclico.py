#solucion por turno ciclico

import threading
import time
from filosofos import main

class Filosofo(threading.Thread):
    semaforo = threading.Lock() 
    def __init__(self,name):
        super().__init__()
        self.comiendo = False
        self.pensando = True
        self.izquierda = False
        self.derecha =False
        self.name = name

    def comer(self):
        self.izquierda = not self.izquierda
        self.derecha = not self.derecha #el filosofo tiene tenedores en ambas manos
        self.pensando=False
        self.comiendo=True
        print('El filosofo '+self.name+' esta comiendo')
        time.sleep(2) #TIEMPO ARBITRARIO PARA COMER
        self.izquierda = not self.izquierda
        self.derecha = not self.derecha #el filosofo ya no tiene tenedores en ambas manos
    def pasarTurno(self):
        self.comer = not self.comer
        print('El filosofo '+self.name+' dejo de comer')

    def run(self):
        self.semaforo.acquire()
        self.comer()
        self.pasarTurno()
        self.semaforo.release()

def main():
    mesa = []
    for i in range(5):
        mesa.append(Filosofo(name='Filosofo '+str(i))) # filosofos llegan a la mesa
        print(mesa[i])
    for f in mesa:
        f.start()
    for f in mesa:
        f.join()

if __name__=="__main__":
    main()