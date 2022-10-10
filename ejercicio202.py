class Cuenta:
    def __init__(self,titular,monto):
        self.titular=titular
        self.monto=monto

    def imprimir(self):
        print("titular:",self.titular)
        print("monto:",self.monto)


class CajaAhorro(Cuenta):

    def __init__(self,titular,monto):
        super().__init__(titular,monto)

    def imprimir(self):
        print("cuenta de caja de ahorro")
        super().imprimir()

class PlazoFijo(Cuenta):

    def __init__(self,titular,monto,plazo,interes):
        super().__init__(titular,monto)
        self.plazo=plazo
        self.interes=interes

    def imprimir(self):
        print("cuenta de plazo fijo")
        super().imprimir()
        print("plazo en dias:",self.plazo)
        print("intereses:",self.interes)
        self.ganancia_interes()

    def ganancia_interes(self):
        ganancia=self.monto*self.interes/100
        print("importe del interes:",ganancia)


cajaahorro=CajaAhorro("pepe", 2000)
cajaahorro.imprimir()

plazofijo=PlazoFijo("lula", 1000, 30, 0.10)
plazofijo.imprimir()
