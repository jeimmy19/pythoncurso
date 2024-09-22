from datetime import datetime

def formato_iso8601(dia, mes, anio):
    try:
       
        fecha = datetime(anio, mes, dia)
        fecha_iso = fecha.strftime("%Y-%m-%d")  
        return fecha_iso
    except ValueError:
        
        return None


dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año:"))

fecha_iso8601 = formato_iso8601(dia, mes, anio)

if fecha_iso8601:
    print(f"Fecha en formato ISO 8601: {fecha_iso8601}")
else:
    print("None")
