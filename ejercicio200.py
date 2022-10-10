class Persona:
    def __init__(self):
        self.nombre=input("ingrese el nombre:")
        self.edad=int(input("ingrese la edad:"))

    def imprimir(self):
        print("nombre:",self.nombre)
        print("edad:",self.edad)


class Empleado(Persona): #herencia

    def __init__(self):
        super().__init__()
        self.sueldo=float(input("ingrese el sueldo:"))

    def imprimir(self):
        super().imprimir()
        print("sueldo:",self.sueldo)

    def paga_impuestos(self):
        if self.sueldo>3000:
            print("el empleado debe pagar impuestos")
        else:
            print("no paga impuestos")



empleado1=Empleado()
empleado1.imprimir()
empleado1.paga_impuestos()
