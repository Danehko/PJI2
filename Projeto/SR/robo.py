from ev3dev.ev3 import *
from Partida import *
from Coordenadas import *
from time import sleep

class Robo:

    def __init__(self,motorA,motorB,velocidade,posx,posy,ref):
        self.coordenadas = Coordenadas(posx,posy,ref)
        self.modoDeJogo = 0  # mododeJogo igual a 0 para modo autonomo e 1 para modo manual
        self.velocidade = velocidade
        self.partida = Partida()
        self.l = LargeMotor(motorA)
        self.r = LargeMotor(motorB)
        self.cl = ColorSensor()
        self.colors = ('unknown', 'black', 'blue', 'green', 'yellow', 'red', 'white', 'brown')
        self.enviar = 0

    def setVol(self):
        return self.velocidade

    def setFrente(self):
        self.cl.mode = 'COL-COLOR'
        if self.colors[self.cl.value()] == "green" or self.colors[self.cl.value()] == "yellow" or self.colors[
            self.cl.value()] == "blue":
            while self.colors[self.cl.value()] == "green" or self.colors[self.cl.value()] == "yellow" or \
                    self.colors[
                        self.cl.value()] == "blue":
                self.r.run_forever(speed_sp=self.velocidade)
                self.l.run_forever(speed_sp=self.velocidade)
            else:
                self.setParar()
        if self.colors[self.cl.value()] == "unknown":
            while self.colors[self.cl.value()] != "black":
                self.r.run_forever(speed_sp=self.velocidade)
        while self.colors[self.cl.value()] != "green":
            while self.colors[self.cl.value()] == "black":
                self.r.run_forever(speed_sp=self.velocidade / 2)
                self.l.run_forever(speed_sp=self.velocidade)
            while self.colors[self.cl.value()] == "white":
                self.r.run_forever(speed_sp=self.velocidade)
                self.l.run_forever(speed_sp=self.velocidade / 2)
            if self.colors[self.cl.value()] == "yellow":
                self.l.run_forever(speed_sp=self.velocidade)
                self.r.run_forever(speed_sp=self.velocidade)
                sleep(0.1)
                break
            if self.colors[self.cl.value()] == "blue":
                self.l.run_forever(speed_sp=self.velocidade)
                self.r.run_forever(speed_sp=self.velocidade)
                sleep(0.1)
                break
        else:
            self.l.run_forever(speed_sp=self.velocidade)
            self.r.run_forever(speed_sp=self.velocidade)
            sleep(0.1)
        self.setParar()

    def setEsquerda(self):
        self.cl.mode = 'COL-COLOR'
        while self.colors[self.cl.value()] == "green":
            self.r.run_forever(speed_sp=self.velocidade)
            self.l.run_forever(speed_sp=self.velocidade * 0)
        else:
            self.l.stop(stop_action="hold")
        while self.colors[self.cl.value()] == "black":
            self.r.run_forever(speed_sp=self.velocidade)
        while self.colors[self.cl.value()] != "black":
            self.r.run_forever(speed_sp=self.velocidade)
        else:
            self.r.run_forever(speed_sp=self.velocidade)
        self.setFrente()

    def setDireita(self):
        self.cl.mode = 'COL-COLOR'
        while self.colors[self.cl.value()] == "green":
            self.l.run_forever(speed_sp=self.velocidade)
            self.r.run_forever(speed_sp=self.velocidade/2)
        else:
            self.r.stop(stop_action="hold")
        while self.colors[self.cl.value()] == "black":
            self.l.run_forever(speed_sp=self.velocidade)
        while self.colors[self.cl.value()] != "black":
            self.l.run_forever(speed_sp=self.velocidade)
        else:
            self.l.run_forever(speed_sp=self.velocidade)
        self.setFrente()

    def setRetornar(self):
        self.cl.mode = 'COL-COLOR'
        while self.colors[self.cl.value()] == "green":
            self.l.run_forever(speed_sp=-self.velocidade)
        while self.colors[self.cl.value()] == "black":
            self.l.run_forever(speed_sp=-self.velocidade)
        while self.colors[self.cl.value()] != "black":
            self.l.run_forever(speed_sp=-self.velocidade)
        self.setParar()
        self.setFrente()

    def setVelocidade(self, setV):
        self.velocidade = setV

    def setParar(self):
        self.r.stop(stop_action="hold")
        self.l.stop(stop_action="hold")

    def autoEsquerda(self):
        x, y = self.coordenadas.verificandoPos('esquerda')
        lista = []
        lista.append((x,y))
        if ((lista in self.partida.localizacaoRobo) or x<0 or x>(6) or y<0 or y>6):
            pass
        else:
            self.coordenadas.trocarPosicao(x,y)
            self.setEsquerda()
            print(self.coordenadas.enviarCoordenadas())
            self.enviar = 1

    def autoDireita(self):
        x, y = self.coordenadas.verificandoPos('direita')
        lista = []
        lista.append((x,y))
        if ((lista in self.partida.localizacaoRobo) or x < 0 or x > 6 or y < 0 or y > 6):
            pass
        else:
            self.coordenadas.trocarPosicao(x, y)
            self.setDireita()
            print(self.coordenadas.enviarCoordenadas())
            self.enviar = 1

    def autoFrente(self):
        x, y = self.coordenadas.verificandoPos('frente')
        lista = []
        lista.append((x,y))
        if ((lista in self.partida.localizacaoRobo) or x < 0 or x > 6 or y < 0 or y > 6):
            pass
        else:
            self.coordenadas.trocarPosicao(x, y)
            self.setFrente()
            print(self.coordenadas.enviarCoordenadas())
            self.enviar = 1

    def autoRetornar(self):
        x, y = self.coordenadas.verificandoPos('retornar')
        lista = []
        lista.append((x,y))
        if ((lista in self.partida.localizacaoRobo) or x < 0 or x > 6 or y < 0 or y > 6):
            pass
        else:
            self.coordenadas.trocarPosicao(x, y)
            self.setRetornar()
            print(self.coordenadas.enviarCoordenadas())
            self.enviar = 1

    def auto(self,_lista):
        x,y = _lista[0]
        aux1 = abs(self.coordenadas.posx - x)
        aux2 = abs(self.coordenadas.posy - y)
        if(aux1<aux2):
            print(self.coordenadas.posx, self.coordenadas.posy)
            if((self.coordenadas.posx == x) and (self.coordenadas.posy == y)):
                time.sleep(2)
                self.enviar = 2
            elif(self.coordenadas.posx > x):
                if(self.coordenadas.ref == 'N'):
                    self.autoEsquerda()
                elif(self.coordenadas.ref == 'S'):
                    self.autoDireita()
                elif(self.coordenadas.ref == 'L'):
                    self.autoRetornar()
                elif(self.coordenadas.ref == 'O'):
                    self.autoFrente()
            elif(self.coordenadas.posx < x):
                if(self.coordenadas.ref == 'N'):
                    self.autoDireita()
                elif(self.coordenadas.ref == 'S'):
                    self.autoEsquerda()
                elif(self.coordenadas.ref == 'L'):
                    self.autoFrente()
                elif(self.coordenadas.ref == 'O'):
                    self.autoRetornar()
            elif(self.coordenadas.posy > y):
                if(self.coordenadas.ref == 'N'):
                    self.autoRetornar()
                elif(self.coordenadas.ref == 'S'):
                    self.autoFrente()
                elif(self.coordenadas.ref == 'L'):
                    self.autoDireita()
                elif(self.coordenadas.ref == 'O'):
                    self.autoEsquerda()
            elif(self.coordenadas.posy < y):
                if(self.coordenadas.ref == 'N'):
                    self.autoFrente()
                elif(self.coordenadas.ref == 'S'):
                    self.autoRetornar()
                elif(self.coordenadas.ref == 'L'):
                    self.autoEsquerda()
                elif(self.coordenadas.ref == 'O'):
                    self.autoDireita()
        else:
            print(self.coordenadas.posx, self.coordenadas.posy)
            if((self.coordenadas.posx == x) and (self.coordenadas.posy == y)):
                self.enviar = 2
                time.sleep(2)
            elif(self.coordenadas.posy > y):
                if(self.coordenadas.ref == 'N'):
                    self.autoRetornar()
                elif(self.coordenadas.ref == 'S'):
                    self.autoFrente()
                elif(self.coordenadas.ref == 'L'):
                    self.autoDireita()
                elif(self.coordenadas.ref == 'O'):
                    self.autoEsquerda()
            elif(self.coordenadas.posy < y):
                if(self.coordenadas.ref == 'N'):
                    self.autoFrente()
                elif(self.coordenadas.ref == 'S'):
                    self.autoRetornar()
                elif(self.coordenadas.ref == 'L'):
                    self.autoEsquerda()
                elif(self.coordenadas.ref == 'O'):
                    self.autoDireita()
            elif(self.coordenadas.posx > x):
                if(self.coordenadas.ref == 'N'):
                    self.autoEsquerda()
                elif(self.coordenadas.ref == 'S'):
                    self.autoDireita()
                elif(self.coordenadas.ref == 'L'):
                    self.autoRetornar()
                elif(self.coordenadas.ref == 'O'):
                    self.autoFrente()
            elif(self.coordenadas.posx < x):
                if(self.coordenadas.ref == 'N'):
                    self.autoDireita()
                elif(self.coordenadas.ref == 'S'):
                    self.autoEsquerda()
                elif(self.coordenadas.ref == 'L'):
                    self.autoFrente()
                elif(self.coordenadas.ref == 'O'):
                    self.autoRetornar()
