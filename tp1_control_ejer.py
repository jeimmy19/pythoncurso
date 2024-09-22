#ejercicio 1 
print("ejercicio 1")
# se pide ingresar los datos de la fecha
dia = int(input("Ingrese el día : "))
mes = int(input("Ingrese el mes : "))
anio = int(input("Ingrese el año (4 dígitos): "))

# Verificar si la fecha es válida puse hasta el año en curso 
if (1 <= dia <= 31) and (1 <= mes <= 12) and (1000 <= anio <= 2023):
    # Verificar febrero
    if mes == 2 and (dia <= 28 or (dia == 29 and ((anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0))):
        print("Fecha válida")
    elif (mes in [4, 6, 9, 11]) and (dia <= 30):
        print("Fecha válida")
    elif (mes in [1, 3, 5, 7, 8, 10, 12]) and (dia <= 31):
        print("Fecha válida")
    else:
        print("Fecha inválida")
else:
    print("Fecha inválida")


#ejercicio 2 
print("ejercicio 2")
## Generar el listado de fichas de dominó
fichas = []
for i in range(7):
    for j in range(i, 7):
        fichas.append((i, j))

# Imprimir las fichas sin duplicados
for ficha in fichas:
    print(f"{ficha[0]}-{ficha[1]}")

# ejercicio 3 

print("ejercicio 3")

segundos = int(input("Ingrese el tiempo en segundos: "))

if segundos < 0:
    print("Error: El valor ingresado debe ser un número no negativo.")
elif segundos == 0:
    print("Tiempo en formato HH:MM:SS: 00:00:00")
elif segundos > 86400:
    print("Error: El valor ingresado supera las 24 horas de 1 dia")
else:
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60

    hora_formateada = f"{horas:02d}"
    minuto_formateado = f"{minutos:02d}"
    segundo_formateado = f"{segundos_restantes:02d}"

    print(f"Tiempo en formato HH:MM:SS: {hora_formateada}:{minuto_formateado}:{segundo_formateado}")

# ejercicio 4 

print("ejercicio 4")

while True:
    peso_galletita = float(input("Ingrese el peso de una galletita (en gramos): "))
    peso_paquete = float(input("Ingrese el peso deseado del paquete en gramos: "))
    peso_acumulado = 0
    tandas = 0

    while True:
        peso_acumulado += peso_galletita
        tandas += 1

        if peso_acumulado >= peso_paquete:
            print(f"Paquete con  {tandas} galletas listo. Peso acumulado: {peso_acumulado} gramos.")
            break

    cambiar_paquete = input("¿Desea cambiar el peso del paquete? (S/N): ").strip().upper()
    if cambiar_paquete != 'S':
        break

print("Programa terminado.")

# ejercicio 5 

print("ejercicio 5")

while True:
    capacidad_silo = float(input("Ingrese la capacidad del silo de harina en kilogramos: "))
    cantidad_harina = float(input("Ingrese la cantidad de harina requerida para la preparación en kilogramos: "))
    harina_restante = 0
    cambiar_silo = "S"

    while cambiar_silo == "S":
        if cantidad_harina <= capacidad_silo:
            print("La cantidad de harina en el silo es suficiente para la preparación.")
            harina_restante = capacidad_silo - cantidad_harina
            print("Harina restante en el silo:", harina_restante, "kg")
            
            preparar_otra = input("¿Desea realizar otra preparación? (S/N): ").strip().upper()
            if preparar_otra == "S":
                cambiar_silo = "N"
                if harina_restante >0:
                     print("La cantidad de harina en el silo es suficiente para la preparación.")
                     cantidad_harina = float(input("Ingrese la cantidad de harina requerida para la preparación en kilogramos: "))
                     if cantidad_harina <= harina_restante:
                        harina_restante = harina_restante - cantidad_harina
                        print("Harina restante en el silo:", harina_restante, "kg")
                     else:
                         print("La cantidad de harina en el silo no es suficiente para la preparación. Preparación cancelada.")
                         cambiar_silo = "N"

        else:
            print("La cantidad de harina en el silo no es suficiente para la preparación. Preparación cancelada.")
            cambiar_silo = "N"

    cambiar_silo = input("¿Desea cambiar la capacidad del silo? (S/N): ").strip().upper()
    if cambiar_silo != "S":
        break

print("Programa terminado.")
