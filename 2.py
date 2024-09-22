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
	while True:

            opc=input("Ingrese que desea realizar: ")
            

            if opc =="N" or opc=="n":

                limpiar()
                opc= "N"
                return opc
		
            elif opc =="E" or opc=="e":
		
                limpiar()
                opc= "E"
                return opc
		
            elif opc =="B" or opc=="b":
		
                limpiar()
                opc="B"
                return opc
            	
            elif opc =="S" or opc =="s":
                limpiar()
                opc= "S"
                return opc
            
            else :
             print ("opcion no valida")
             t=2
             time.sleep(t)


opcion=menu()
print("La opcion es:",opcion)
t=2
time.sleep(t)

		
		 