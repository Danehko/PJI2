class Coordenadas:
    def __init__(self,posx,posy,ref):
        self.posx = posx
        self.posy = posy
        self.ref = ref
        self.nextRef = 'SR'
        self.habilitarTroca = 0

    def enviarCoordenadas(self):
        return (self.posx, self.posy)

    def trocarPosicao(self, x, y):
        if(self.habilitarTroca == 1):
            self.posx = x
            self.posy = y
            self.ref = self.nextRef
            self.nextRef = 'SR'
            self.habilitarTroca = 0

    def verificandoPos(self, dir): #trocandoPos
        if(dir=='frente'):
            if(self.ref=='N'):
                self.nextRef = self.ref
                self.habilitarTroca = 1
                return(self.posx, (self.posy + 1))
            elif(self.ref=='S'):
                self.nextRef = self.ref
                self.habilitarTroca = 1
                return(self.posx, (self.posy - 1))
            elif (self.ref == 'L'):
                self.nextRef = self.ref
                self.habilitarTroca = 1
                return((self.posx + 1), self.posy)
            elif (self.ref == 'O'):
                self.nextRef = self.ref
                self.habilitarTroca = 1
                return((self.posx - 1), self.posy)
        elif(dir=='retornar'):
            if (self.ref == 'N'):
                self.nextRef = 'S'
                self.habilitarTroca = 1
                return(self.posx, (self.posy - 1))
            elif (self.ref == 'S'):
                self.nextRef = 'N'
                self.habilitarTroca = 1                
                return(self.posx, (self.posy + 1))
            elif (self.ref == 'L'):
                self.nextRef = 'O'
                self.habilitarTroca = 1
                return((self.posx - 1), self.posy)
            elif (self.ref == 'O'):
                self.nextRef = 'L'
                self.habilitarTroca = 1
                return((self.posx + 1), self.posy)
        elif (dir == 'direita'):
            if (self.ref == 'N'):
                self.nextRef = 'L'
                self.habilitarTroca = 1
                return((self.posx + 1), self.posy)
            elif (self.ref == 'S'):
                self.nextRef = 'O'
                self.habilitarTroca = 1
                return((self.posx - 1), self.posy)
            elif (self.ref == 'L'):
                self.nextRef = 'S'
                self.habilitarTroca = 1
                return(self.posx, (self.posy - 1))
            elif (self.ref == 'O'):
                self.nextRef = 'N'
                self.habilitarTroca = 1
                return(self.posx, (self.posy + 1))
        elif (dir == 'esquerda'):
            if (self.ref == 'N'):
                self.nextRef = 'O'
                self.habilitarTroca = 1
                return((self.posx - 1), self.posy)
            elif (self.ref == 'S'):
                self.nextRef = 'L'
                self.habilitarTroca = 1
                return((self.posx + 1), self.posy)
            elif (self.ref == 'L'):
                self.nextRef = 'N'
                self.habilitarTroca = 1
                return(self.posx, (self.posy + 1))
            elif (self.ref == 'O'):
                self.nextRef = 'S'
                self.habilitarTroca = 1
                return(self.posx, (self.posy - 1))
