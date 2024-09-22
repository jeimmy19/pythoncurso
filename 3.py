def menu(diccionario):
    while True:
        print("Seleccione una opción:")
        for key, value in diccionario.items():
            print(f"{key}: {value}")

        opcion_seleccionada = input("Ingrese el número de la opción seleccionada: ")

        if opcion_seleccionada in diccionario:
            return opcion_seleccionada
        else:
            print("Opción inválida. Intente nuevamente.")

# Programa principal
menu_principal = {'N': 'Nuevo', 'E': 'Editar', 'B': 'Borrar', 'S': 'Salir'}
opcion = menu(menu_principal)
print("Opción seleccionada:", opcion)

menu_ejemplo = {'N': 'Nuevo', 'E': 'Editar', 'B': 'Borrar', 'I': 'Imprimir', 'S': 'Salir'}
opcion_ejemplo = menu(menu_ejemplo)
print("Opción seleccionada:", opcion_ejemplo)

menu_clientes = {'N': 'Nuevo Cliente', 'B': 'Buscar Cliente', 'A': 'Actualizar datos del cliente', 'X': 'Borrar cliente'}
opcion_clientes = menu(menu_clientes)
print("Opción seleccionada:", opcion_clientes)
