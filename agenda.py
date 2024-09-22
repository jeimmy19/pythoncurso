class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}"

class Agenda:
    def __init__(self):
        self.contactos = []

    def añadir_contacto(self):
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el teléfono del contacto: ")
        email = input("Ingrese el email del contacto: ")
        nuevo_contacto = Contacto(nombre, telefono, email)
        self.contactos.append(nuevo_contacto)
        print("Contacto añadido con éxito.")

    def listar_contactos(self):
        if not self.contactos:
            print("No hay contactos en la agenda.")
        else:
            print("Lista de contactos:")
            for contacto in self.contactos:
                print(contacto)

    def buscar_contacto(self):
        nombre = input("Ingrese el nombre del contacto que desea buscar: ")
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                print("Contacto encontrado:")
                print(contacto)
                return
        print("Contacto no encontrado.")

    def editar_contacto(self):
        nombre = input("Ingrese el nombre del contacto que desea editar: ")
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                print("Editando contacto:")
                print(contacto)
                contacto.nombre = input("Nuevo nombre: ") or contacto.nombre
                contacto.telefono = input("Nuevo teléfono: ") or contacto.telefono
                contacto.email = input("Nuevo email: ") or contacto.email
                print("Contacto actualizado con éxito.")
                return
        print("Contacto no encontrado.")

    def mostrar_menu(self):
        while True:
            print("\n--- Menú de Agenda ---")
            print("1. Añadir contacto")
            print("2. Lista de contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")
            opcion = input("Seleccione una opción (1-5): ")

            if opcion == '1':
                self.añadir_contacto()
            elif opcion == '2':
                self.listar_contactos()
            elif opcion == '3':
                self.buscar_contacto()
            elif opcion == '4':
                self.editar_contacto()
            elif opcion == '5':
                print("Cerrando la agenda...")
                break
            else:
                print("Opción no válida, intente de nuevo.")

# Crear una instancia de la agenda y mostrar el menú
mi_agenda = Agenda()
mi_agenda.mostrar_menu()
