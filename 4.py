def ingresar_datos_cliente():
    nombre_empresa = input("Ingrese el nombre de la empresa: ")
    nombre_contacto = input("Ingrese el nombre del contacto: ")
    email = input("Ingrese el correo electrónico: ")

    return (nombre_empresa, nombre_contacto, email)

datos_cliente = ingresar_datos_cliente()
print("Datos del cliente ingresados:", datos_cliente)
