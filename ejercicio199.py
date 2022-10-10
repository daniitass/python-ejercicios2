class Socio:
    def __init__(self):
        self.nombre=input("ingrese el nombre del socio:")
        self.antiguedad=int(input("ingrese la antiguedad:"))

    def imprimir(self):
        print(self.nombre,"tiene una antigüedad de",self.antiguedad)

    def retornar_antiguedad(self):
        return self.antiguedad


class Club:
    def __init__(self):
        self.socio1=Socio()
        self.socio2=Socio()
        self.socio3=Socio()

    def mayor_antiguedad(self):
        print("el socio con mayor antigüedad es ")
        if (self.socio1.retornar_antiguedad()>self.socio2.retornar_antiguedad() and
            self.socio1.retornar_antiguedad()>self.socio3.retornar_antiguedad()):
            self.socio1.imprimir()
        else:
            if self.socio2.retornar_antiguedad()>self.socio3.retornar_antiguedad():
                self.socio2.imprimir()
            else:
                self.socio3.imprimir()

club=Club()
club.mayor_antiguedad()
