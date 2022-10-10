class alumnos:
    def __init__(self):
        self.nombres=[]
        self.notas=[]
    def menu(self):
       opcion=0
       while opcion != 4:
           print ("1 es cargar ")
           print ("2 es listar alumnos")
           print ("3 aprobados")
           print ("4 finalizar")
           print (" ")
           opcion = int(input("ingrese la opcion"))
           print (" ")
           if opcion == 1:
               self.cargar()
           else:
                if opcion ==2 :
                    self.listar()
                else:
                    if opcion == 3 :
                        self.aprobados()
    def cargar (self):
        for x in range(5):
            nombre=input ("ingrese un nombre")
            nota= int (input("ingrese la nota"))
            self.nombres.append(nombre)
            self.notas.append(nota)
    def listar(self):
        for x in range(5):
            print (self.nombres[x], " su nota es" ,self.notas[x])
    def aprobados(self):
        for x in range (5):
            if self.notas[x] >= 7 :
                print ("los aprobados son", self.nombres[x])
alumnos=alumnos()
alumnos.menu()
