#Programa que calcule la raíz de una función usando el método de Newton-Raphson
#Autores: Diego Burgos y Luis Carreyó
#Fecha: 28/05/2022

#Importamos las librerías necesarias
import imp
import math
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

#Subimos la gráfica de la función

#Establecemos la función y el intervalo de búsqueda

x = sp.Symbol('x')
f = x**3 + 2*x - 5
fx = lambda x: x**3 + 2*x - 5
x_0 = float(input("Introduce el valor inicial: "))
tol = 0.01

#Derivamos la función usando librerías de Python

df = f.diff(x)
dfx = lambda x: df
print(df)

#Valores iniciales de la tabla de iteraciones

tabla_iteraciones = []
tramo = abs(2*tol)
x_i = x_0

#Realizamos el ciclo para que el programa se repita hasta encontrar la raíz

while (tramo>=tol):
    xnuevo = xi - fx(xi)/dfx(xi)
    tramo  = abs(xnuevo-xi)
    tabla_iteraciones.append([xi,xnuevo,tramo])
    xi = xnuevo

tabla = np.array(tabla_iteraciones)
n = len(tabla)

#Mostramos la tabla de iteraciones

print(['xi', 'xnuevo', 'tramo'])
np.set_printoptions(precision = 4)
print(tabla)
print('raiz en: ', xi)
print('con error de: ',tramo)


