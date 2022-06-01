#Programa que calcule la raíz de una función usando el método de Newton-Raphson
#Autores: Diego Burgos y Luis Carreyó
#Fecha: 28/05/2022

#Importamos las librerías necesarias
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

#Subimos la gráfica de la función

#El usuario introduce la función

c1 = float(input("Introduce el valor del primer coeficiente: "))
e1 = float(input("Introduce el valor del primer exponente: "))

c2 = float(input("Introduce el valor del segundo coeficiente: "))
e2 = float(input("Introduce el valor del segundo exponente: "))

c3 = float(input("Introduce el valor del tercer coeficiente: "))
e3 = float(input("Introduce el valor del tercer exponente: "))

#Establecemos la función y el intervalo de búsqueda

dx = sp.Symbol('x') #Symbol es una función de Sympy que permite crear variables
f = lambda x: c1*x**e1 + c2*x**e2 + c3*x**e3
fx = c1*dx**e1 + c2*dx**e2 + c3*dx**e3
x_0 = float(input("Introduce el valor inicial: "))
tol = 0.01

#Derivamos la función usando librerías de Python

df = sp.diff(f(dx),dx) #Diff es una función de Sympy que permite derivar una función
dfx = sp.lambdify(dx,df) 
#Lambdify es una función de Sympy que permite evaluar una función tal como hace Lambda en Numpy


#Muestra la función establecida por el usuario y su derivada

print("La función es: ",fx)
print("La derivada de la función es: ", df)

#Valores iniciales de la tabla de iteraciones

i = 1
tabla_iteraciones = []
tramo = abs(2*tol)
x_i = x_0

#Realizamos el ciclo para que el programa se repita hasta encontrar la raíz

while (tramo>tol):
    x_nuevo = x_i - f(x_i)/dfx(x_i)
    tramo  = abs(x_nuevo-x_i)
    tabla_iteraciones.append([i,x_i,x_nuevo,tramo])
    x_i = x_nuevo
    i = i + 1

tabla = np.array(tabla_iteraciones)
n = len(tabla)

#Mostramos la tabla de iteraciones

print('i', ' x_i ', ' x_nuevo ', ' error ')
np.set_printoptions(precision = 4, suppress = True)
print(tabla)

print('Raíz: ', x_i)