def imprimir_datos_producto(datos_producto):
    if len(datos_producto) == 4:
        marca, modelo, precio, stock = datos_producto
        print("Datos del Producto:")
        print(f"Marca: {marca}")
        print(f"Modelo: {modelo}")
        print(f"Precio: {precio}")
        print(f"Stock Disponible: {stock}")
    else:
        print("Error: La lista de datos del producto debe contener exactamente 4 elementos.")

def main():
    listas_productos = []

    while True:
        print("\nMenú:")
        print("1. Crear lista de producto")
        print("2. Imprimir lista de productos")
        print("3. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            marca = input("Ingrese la marca del producto: ")
            modelo = input("Ingrese el modelo del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            stock = int(input("Ingrese el stock disponible del producto: "))

            nuevo_producto = [marca, modelo, precio, stock]
            listas_productos.append(nuevo_producto)

        elif opcion == "2":
            if listas_productos:
                for i, producto in enumerate(listas_productos, 1):
                    print(f"\nProducto {i}:")
                    imprimir_datos_producto(producto)
            else:
                print("No hay listas de productos para mostrar.")

        elif opcion == "3":
            print("Saliendo del programa.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
