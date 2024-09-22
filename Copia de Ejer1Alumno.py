#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. 
# Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si 
# ha aprobado o no.

class Alumno:
	def inicializar(self, nombre, nota):  # inicializamos atributos
		self.nombre = nombre
		self.nota = nota
	def imprimir(self):                   # funcion para imprimir los datos
		print("Nombre: ", self.nombre)
		print("Nota: ", self.nota)
	def resultado(self):                  # funcion para obtener los datos
		if self.nota < 4:
			print("El alumno ha Desaprobado")
		else:
			print("El alumno ha Aprobado")

# bloque principal
# creamos los nuevos objetos
alumno1 = Alumno()
alumno2 = Alumno()

# inicializamos los atributos
alumno1.inicializar("Mariana", 8)
alumno2.inicializar("Juan", 3)

# imprimimos los datos y resultados de cada alumno
alumno1.imprimir()
alumno1.resultado()
alumno2.imprimir()
alumno2.resultado()
