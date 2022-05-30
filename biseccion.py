#Programa que calcule la raíz de una función que introduzca el usuario
#Autores: Diego Burgos y Luis Carreyó
#Fecha: 22/05/2022

#Importamos las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt

#Subimos la gráfica de la función

#Establecemos la función y el intervalo de búsqueda junto con la tolerancia

f = lambda x: -0.5*x**2 + 2.5*x + 4.5
x_a = float(input("Introduce el valor del límite inferior: "))
x_b = float(input("Introduce el valor de límite superior: "))
tol = 0.01

#Realizamos los procesos iniciales antes de la búsqueda

intervalo = x_b - x_a #Representa el intervalo de búsqueda entre los límites
#Entre más pequeño sea el intervalo, más precisa será la raíz
fa = f(x_a)
fb = f(x_b)
i = 1
tabla_iteraciones = []

#Ciclo que realiza la búsqueda de la raíz

while (intervalo>tol):
        
    x_r = (x_a + x_b) / 2
    fx = f(x_r)
    tabla_iteraciones.append([i,x_a,x_b,x_r,fa,fb,fx,intervalo])
    i = i + 1

    nuevo = np.sign(fa)*np.sign(fx) #Determina si debemos seguir buscando en el límite inferior o superior con el signo

    if (nuevo > 0):
        x_a = x_r
        fa = fx
        intervalo = x_b - x_a
    if (nuevo < 0):
        x_b = x_r
        fb = fx
        intervalo = x_b - x_a

x_r = (x_a + x_b) / 2
fx = f(x_r)
tabla_iteraciones.append([i,x_a,x_b,x_r,fa,fb,fx,intervalo])
raíz = x_r


#Mostramos la tabla de iteraciones

np.set_printoptions(precision = 4)
print('i', ' inf ', ' sup ', ' raíz ', 'evinf', 'evsup', 'evraíz', 'error')

n=len(tabla_iteraciones)
for i in range(0,n,1):
    unafila = tabla_iteraciones[i]
    formato = '{:.0f}'+' '+(len(unafila)-1)*'{:.3f} '
    unafila = formato.format(*unafila)
    print(unafila)
    
print('Raíz: ', raíz)

