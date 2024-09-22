import os
import time

def limpiar():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        
def menu():
	
	print("Bienvenidos al sistema ")
	print(" ")
	print("Las opciones disponibles son las siguientes: ")
	print(" ")
	print("  #N Nuevo ")
	print("  #E Editar")
	print("  #B Borrar")
	print("  #S Salir")
	print ()
		   
while True:
	limpiar()	
	menu()
	opc=input("Ingrese que desea realizar: ")
	limpiar()

	if opc =="N" or opc=="n":

		limpiar()
		print ("La opcion elegida es: Nuevo")
		t=3
		time.sleep(t)
		
	elif opc =="E" or opc=="e":
		
		limpiar()
		print ("La opcion elegida es: Editar")
		t=3
		time.sleep(t)
		
	elif opc =="B" or opc=="b":
		
		limpiar()
		print ("La opcion elegida es: Borrar")
		t=3
		time.sleep(t)
		
		
	elif opc =="S" or opc =="s":
		print ("La opcion elegida es: Salir")
		break
	
	else :
		print ("opcion no valida")
		t=2
		time.sleep(t)
		
		