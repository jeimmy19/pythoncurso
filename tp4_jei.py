import math

def normalizar_vector(vector):
    
    modulo = math.sqrt(sum(x**2 for x in vector))
    vector_normalizado = [x / modulo for x in vector]
    return vector_normalizado

def eliminar_duplicados(lista):
   
    lista_sin_duplicados = list(set(lista))
    return lista_sin_duplicados

def mostrar_tablero(tablero):
    for i in range(3):
        for j in range(3):
            
            print(tablero[i][j], end="")

           
            if j < 2:
                print(" | ", end="")

        print()  

        
        if i < 2:
            print("---+---+---")

def hay_ganador(tablero):
    
    for i in range(3):
        
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != ' ':
            return tablero[i][0]
        
        
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != ' ':
            return tablero[0][i]

   
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != ' ':
        return tablero[0][0]

    if tablero[0][2] == tablero[1][1] == tablero[2][0] != ' ':
        return tablero[0][2]

    
    return None

   
    if len(vertices) < 3:
      
        raise ValueError("El polígono debe tener al menos 3 vértices.")

    
    area_total = 0.0

    
    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % len(vertices)]  

        
        area_triangular = 0.5 * (x1 * y2 - x2 * y1)

       
        area_total += area_triangular

    
    area_total = abs(area_total)

    return area_total
  
#datos funcion 1 
vector_original = [3.0, 4.0]
vector_normalizado = normalizar_vector(vector_original)
print("Vector original:", vector_original)
print("Vector normalizado:", vector_normalizado)
#datos funcion 2
lista1 = [1, 4, 1, 5, 4, 1]
lista2 = ["Juan", "Luis", "Juan", "Ana", "Luis"]
resultado_lista1 = eliminar_duplicados(lista1)
resultado_lista2 = eliminar_duplicados(lista2)
print("Lista sin duplicados 1:", resultado_lista1)
print("Lista sin duplicados 2:", resultado_lista2)
#datos funcion 3
tablero = [["x", "o", " "], ["o", " ", "x"], ["x", " ", "o"]]
mostrar_tablero(tablero)
#datos funcion 4
tablero1 = [["x", "o", " "], ["o", " ", "x"], ["x", " ", "o"]]
tablero2 = [["x", "o", " "], ["x", "o", "x"], ["x", " ", "o"]]
resultado1 = hay_ganador(tablero1)
resultado2 = hay_ganador(tablero2)
print("Resultado 1:", resultado1)  
print("Resultado 2:", resultado2)
#datos funcion 5
vertices_poligono = [(0, 0), (3, 0), (3, 4), (0, 4)]
superficie = calcular_superficie_poligono(vertices_poligono)
print("Superficie del polígono:", superficie)



