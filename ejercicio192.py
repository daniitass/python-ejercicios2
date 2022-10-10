class Cuadrado():
        def __init__(self,valorLado): # lado como parametro
            self.lado=valorLado #atributo que recibe el parametro

        def mostrar_perimetro(self):
            per=self.lado*4
            print("El perimetro del cuadrado es:",per)
        def mostrar_superficie(self):
            sup=self.lado*self.lado
            print("La superficie del cuadrado es:",sup)

cuadrado1=Cuadrado(2)
cuadrado1.mostrar_perimetro()
cuadrado1.mostrar_superficie()
