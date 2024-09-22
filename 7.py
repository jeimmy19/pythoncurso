def imprimir_listado_productos(lista_productos):
    if not lista_productos:
        print("La lista de productos está vacía.")
        return

    print("+" + "-"*68 + "+")
    print("| {:<15} | {:<15} | {:<10} | {:<15}|".format("Marca", "Modelo", "Precio", "Stock Disponible"))
    print("+" + "-"*68 + "+")

    for producto in lista_productos:
        marca, modelo, precio, stock = producto
        print("| {:<15} | {:<15} | ${:<9,.2f} |{:<15}|".format(marca, modelo, precio, stock))

    print("+" + "-"*68 + "+")


lista1 = [("Samsung", "LA5890", 12345, 28),
          ("Samsung", "LB001", 2550, 205),
          ("LG", "GL-2552", 25400, 18)]

lista2 = [("Sony", "A-1205N", 2550, 0)]

lista3 = [("Samsung", "LA5890", 12345, 28),
          ("Samsung", "LB001", 2550, 205),
          ("LG", "GL-2552", 25400, 18),
          ("LG", "GL-3250", 35200, 28),
          ("LG", "GL-5240S", 105800, 0)]

lista4 = []

imprimir_listado_productos(lista1)
print("\n")
imprimir_listado_productos(lista2)
print("\n")
imprimir_listado_productos(lista3)
print("\n")
imprimir_listado_productos(lista4)
