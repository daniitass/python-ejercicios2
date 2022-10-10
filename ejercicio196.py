class Agenda:

    def __init__(self):
        self.contactos={} # diccionario vacio

    def menu(self):
        opcion=0
        while opcion!=5:
            print("1- ingresar un contacto en la agenda")
            print("2- listado completo de la agenda")
            print("3- consulta ingresando el nombre de la persona")
            print("4- modificacion del telefono y mail")
            print("5- finalizar programa")
            opcion=int(input("Ingrese una opcion:"))
            if opcion==1:
                self.cargar()
            elif opcion==2:
                self.listado()
            elif opcion==3:
                self.consulta()
            elif opcion==4:
                self.modificacion()

    def cargar(self):
        nombre=input("Ingrese el nombre de la persona:")
        telefono=input("Ingrese el numero de telefono:")
        mail=input("Ingrese el mail:")
        self.contactos[nombre]=(telefono,mail) #llamo el diccionario y nombre es la clave
        print("______________________________________________")
        
    def listado(self):      
        print("Listado completo de la agenda")
        for nombre in self.contactos: #asi recorre la lista completa
            print(nombre, self.contactos[nombre][0],self.contactos[nombre][1])
        print("______________________________________________")

    def consulta(self):       
        nombre=input("Ingrese el nombre de la persona a consultar:")
        if nombre in self.contactos:
            print(nombre," su telefono es",self.contactos[nombre][0],"y su mail es",self.contactos[nombre][1])
        else:
            print("No existe un contacto con ese nombre")
        print("______________________________________________")            

    def modificacion(self):       
        nombre=input("Ingrese el nombre de la persona a modificar el telefono y mail:")
        if nombre in self.contactos:
            telefono=input("Ingrese el nuevo telefono:")
            mail=input("Ingrese el nuevo mail:")
            self.contactos[nombre]=(telefono,mail) #sobreescribe el dato
        else:
            print("No existe un contaxto con ese nombre")
        print("______________________________________________")         
        

agenda=Agenda()
agenda.menu()
