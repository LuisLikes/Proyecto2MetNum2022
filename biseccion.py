#Programa que calcule la raíz de una función que introduzca el usuario
#Autores: Diego Burgos y Luis Carreyó
#Fecha: 22/05/2022

#Importamos las librerías necesarias
import math
import matplotlib.pyplot as plt

#Subimos la gráfica de la función

#Establecemos la función y el intervalo de búsqueda

f = lambda x: -0.5*x**2 + 2.5*x + 4.5
x_a = float(input("Introduce el valor del límite inferior: "))
x_b = float(input("Introduce el valor de límite superior: "))

#Realizamos el ciclo para que el programa se repita hasta encontrar la raíz

def bisection(fun, x_a, x_b, eps=None, steps=10):

    if eps is not None:
        steps = math.ceil(math.log((x_b - x_a) / eps) / math.log(2))
    
    # Ciclo para realizar el método de la bisección

    for n in range(steps + 1):
        
        x_r = (x_a + x_b) / 2
        
        if f(x_r) == 0:
            return x_r
        
        if f(x_a) * f(x_r) < 0:
            x_b = x_r
            
        else:
            x_a = x_r
    
    return x_r

print("La raíz es: ", bisection(f, x_a, x_b))



