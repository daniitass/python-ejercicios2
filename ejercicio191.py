class Punto:
    def __init__(self,x,y): #recibe como parametros x e y 
        self.x=x
        self.y=y
    def imprimir(self):
        print("Coordenadas del punto:")
        print("( ",self.x,",",self.y,")")
    def imprimir_cuadrante(self):
        if self.x>0 and self.y>0:
            print("Primer cuadrange")
        else:
            if self.x<0 and self.y>0:
                print("Segundo cuadrante")
            else:
                if self.x<0 and self.y<0:
                    print("Tercer cuadrante")
                else:
                    if self.x>0 and self.y<0:
                        print("Cuarto cuadrante")
punto1 = Punto(8,-10)
punto1.imprimir()
punto1.imprimir_cuadrante()
