#Programa que calcule la raíz de una función que introduzca el usuario
#Autores: Diego Burgos y Luis Carreyó
#Fecha: 22/05/2022

#Importamos las librerías necesarias
import math
from re import X
import numpy as np
import matplotlib.pyplot as plt

#Definimos la función que vamos a utilizar

f = lambda x: -0.5*x**2 + 2.5*x + 4.5

#Importamos la gráfica de la función

plt.plot(np.linspace(-5,5,100),f(np.linspace(-5,5,100)))
plt.show()

#Introducimos los valores iniciales y la tolerancia

print("Una vez vista la gráfica, introduzca los valores iniciales.")
a = float(input("Introduce el valor inicial del límite inferior: "))
b = float(input("Introduce el valor inicial del límite superior: "))
tol = 0.01

#Ciclo que realiza el cálculo de la raíz

#Calculamos el error

error = abs(b-a)

while error > tol:
    
    #Calculamos el punto medio

    x = lambda a,b: (a+b)/2

    if f(a)*f(x) < 0:
        b = x
    else:
        a = x





