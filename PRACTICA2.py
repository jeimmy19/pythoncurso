import math
def calcular_distancia(x1, y1, x2, y2):
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distancia

def volumen_caja(ancho, alto, profundidad):
  
  # Calculamos el volumen de la caja.
  volumencm= ancho * alto* profundidad
  volumen=volumencm/1000

  return volumen

def encriptar(texto, clave):

  # Convertimos el texto a código ASCII.
  texto_ascii = [ord(letra) for letra in texto]

  # Aplicamos el desplazamiento a cada letra.
  for i in range(len(texto_ascii)):
    # Solo encriptamos las letras del abecedario.
    if 97 <= texto_ascii[i] <= 122:
      texto_ascii[i] = texto_ascii[i] + clave % 26

  # Convertimos el código ASCII a texto.
  texto_encriptado = ''.join([chr(letra) for letra in texto_ascii])

  return texto_encriptado

def desencriptar(texto, clave):
 
  # Convertimos el texto a código ASCII.
  texto_ascii = [ord(letra) for letra in texto]

  # Aplicamos el desplazamiento inverso a cada letra.
  for i in range(len(texto_ascii)):
    texto_ascii[i] = texto_ascii[i] - clave

  # Convertimos el código ASCII a texto.
  texto_desencriptado = ''.join([chr(letra) for letra in texto_ascii])

  return texto_desencriptado

def calcular_rollos_empapelado(largo, ancho, alto, ancho_rollo_cm=52, largo_rollo_m=10):
    # Calculamos el área de las paredes a empapelar
    area_paredes = 2 * alto * (largo + ancho)
    
    # Convertimos el ancho del rollo a metros
    ancho_rollo_m = ancho_rollo_cm / 100
    
    # Calculamos cuánto empapelado hay en un solo rollo
    area_rollo = ancho_rollo_m * largo_rollo_m
    
    # Calculamos la cantidad de rollos necesarios
    rollos_necesarios = math.ceil(area_paredes / area_rollo)
    
    return rollos_necesarios

def formatear_nombre(apellido, nombre, nombreseg, mayusculas=False):
    if nombreseg.strip()==" ":
      if mayusculas:
        apellido = apellido.upper()
        nombre = nombre.upper()
        return f"{apellido}, {nombre[0]}."
    else:
        if mayusculas:
            apellido = apellido.upper()
            nombre = nombre.upper()
            nombreseg = nombreseg.upper()
        return f"{apellido}, {nombre[0]}. {nombreseg[0]}."

def menu():
    while True:
        print("\nMenú:")
        print("1. Distancia entre 2 puntos")
        print("2. Volumen en litros de una caja")
        print("3. Encriptar un texto")
        print("4. Desencriptar un texto")
        print("5. Formato de Nombre")
        print("6. Empapelado de una pared")
        print("0. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            x1= int(input("Ingrese punto x1: "))
            y1= int(input("Ingrese punto y1: "))
            x2= int(input("Ingrese punto x2: "))
            y2= int(input("Ingrese punto y2: "))

            distancia= calcular_distancia(x1, y1, x2, y2)

            print ("La distancia de los puntos es: ",distancia )


        elif opcion == '2':
            ancho= int(input("Ingrese ancho de la caja: "))
            alto= int(input("Ingrese alto de la caja: "))
            profundidad = int(input("Ingrese profundidad de la caja: "))
            volumen = volumen_caja(ancho, alto, profundidad)
            print(f"El volumen de la caja es de {volumen} litros.")


        elif opcion == '3':
          texto=input("Ingrese texto a encriptar: ")
          clave=int(input("Ingrese clave para encriptado: "))
          texto_encriptado = encriptar(texto, clave)
          print(texto_encriptado)
        elif opcion == '4':
          texto_desencriptado = desencriptar(texto_encriptado, clave)
          print(texto_desencriptado)
        elif opcion == '5':
          apellido=input ("Ingrese Apellido: ")
          nombre=input ("Ingrese Primer nombre: ")
          nombreseg=input ("Ingrese Segundo nombre: ")
          nombre_completo1 = formatear_nombre(apellido,nombre,nombreseg)
          print(nombre_completo1)  

          
        elif opcion == '6':
          ancho= int(input("Ingrese ancho de la pared: "))
          alto= int(input("Ingrese alto de la pared: "))
          largo= int(input("Ingrese largo de la pared: "))
          cantidad_rollos = calcular_rollos_empapelado(largo,ancho,alto)
          print(f"Se necesitan {cantidad_rollos} rollos de empapelado.")

        elif opcion == '0':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

# Ejecutar el menú
menu()

