#ejercicio 1

for i in range (11):
 multiplicacion = i * 4 
 print(i,"* 4 =", multiplicacion)

#ejercicio 2

suma=0
while suma<10:
 nuevo = int(input ("Ingrese un nuevo numero:"))
 suma=nuevo+suma
 print ("La suma es: ", suma) 

#EJERCICIO 3

for numero in range(1, 13):
    if numero % 2 == 1:
        
        print(f"{numero:2d} |", end=" ")
    else:
      
        print(f" {numero:2d}")


#EJERCICIO 4
for numero in range(1, 13):
    if numero <= 6:
        print(f"{numero:2d} |", end=" ")
    else:
        
        print(f"{numero:2d}")

