from bisect import bisect
from distutils.command.config import LANG_EXT
from doctest import master
from tokenize import String
import numpy as np
from cProfile import label
from ctypes import alignment
from tkinter import *
import tkinter
from turtle import bgcolor
from unittest import result
from matplotlib.pyplot import text
from tkinter import messagebox
import PIL.Image
import PIL.ImageTk
from numpy import bitwise_xor
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
from sympy import true

# Tkinter Interface
bisec = Tk()
bisec.title("Bisección Gay")
bisec.geometry("700x550")
bisec.config(background="#272635")
"""
bisec.iconbitmap("tamal.ico")
"""


def deleteTab():
    bisec.destroy()


def tab2():
    def calcGraf():
        def tab3():
            bisec = Tk()
            bisec.title("Bisección Gay")
            bisec.geometry("700x550")
            bisec.config(background="#272635")
            encabezado = Label(bisec, text="Introduce valores en la ecuación", fg="#A6A6A8", bg="#272635",
                               font=("Berlin Sans FB Demi", 20)).place(x=150, y=20)
            limSup_string = limSup.get()
            x_b = int(limSup_string)
            limInf_string = limInf.get()
            x_a = int(limInf_string)
            tol = 0.01

            # Muestra la función establecida por el usuario

            # Realizamos los procesos iniciales antes de la búsqueda

            intervalo = x_b - x_a  # Representa el intervalo de búsqueda entre los límites
            # Entre más pequeño sea el intervalo, más precisa será la raíz
            fa = f(x_a)
            fb = f(x_b)
            i = 1
            tabla_iteraciones = []

            # Ciclo que realiza la búsqueda de la raíz

            while (intervalo > tol):

                x_r = (x_a + x_b) / 2
                fx = f(x_r)
                tabla_iteraciones.append(
                    [i, x_a, x_b, x_r, fa, fb, fx, intervalo])
                i = i + 1

                # Determina si debemos seguir buscando en el límite inferior o superior con el signo
                nuevo = np.sign(fa)*np.sign(fx)

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
            tabla_iteraciones.append([i, x_a, x_b, x_r, fa, fb, fx, intervalo])
            raíz = x_r

            # Mostramos la tabla de iteraciones

            np.set_printoptions(precision=4)
            descrip = Label(
                bisec, text=' i       inf         sup          raíz         evinf          evsup          evraíz          error', fg="#A6A6A8", bg="#272635",
                font=("Berlin Sans FB Demi", 16)).place(x=30, y=60)
            n = len(tabla_iteraciones)
            for i in range(0, n, 1):
                unafila = tabla_iteraciones[i]
                formato = '{:.0f}'+'   '+(len(unafila)-1)*'{:.3f} '
                unafila = formato.format(*unafila)
                unafila_lab = Label(bisec, text=(unafila, "   "), fg="#A6A6A8", bg="#272635",
                                    font=("Berlin Sans FB Demi", 16)).place(x=10, y=20+50)

            print('Raíz: ', raíz)

        x = np.linspace(-10, 10, 100)

        x2data_string = x2data.get()
        x2data_num = float(x2data_string)
        exp2data_string = exp2data.get()
        exp2data_num = float(exp2data_string)

        x1data_string = x1data.get()
        x1data_num = float(x1data_string)
        exp1data_string = exp1data.get()
        exp1data_num = float(exp1data_string)
        xdata_string = xdata.get()
        xdata_num = float(xdata_string)
        expdata_string = expdata.get()
        expdata_num = float(expdata_string)

        def f(x): return x2data_num*x**exp2data_num+x1data_num * \
            x**exp1data_num+xdata_num*x**expdata_num
        fig = plt.figure(figsize=(4, 3), dpi=100)
        ax = fig.add_subplot(111)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax = plt.plot(x, f(x), 'r')
        ax = FigureCanvasTkAgg(fig, master=bisec)
        ax.get_tk_widget().place(x=30, y=200)
        # Introducir límite superior
        label_limSup = Label(
            bisec, text="Límite Superior:", fg="#A6A6A8", bg="#272635",
            font=("Berlin Sans FB Demi", 16)).place(x=450, y=250)
        limSup = StringVar()
        entry_limSup = Entry(width=5, textvariable=limSup, font=(
            "Berlin Sans FB Demi", 10)).place(x=610, y=255)

        # Introducir límite inferior
        label_limInf = Label(
            bisec, text="Límite Inferior:", fg="#A6A6A8", bg="#272635",
            font=("Berlin Sans FB Demi", 16)).place(x=460, y=310)
        limInf = StringVar()
        entry_limInf = Entry(width=5, textvariable=limInf, font=(
            "Berlin Sans FB Demi", 10)).place(x=610, y=315)
        resultado = Button(bisec, text="Resultado", fg="#FFFFFF", bg="#FFB949", font=("Berlin Sans FB Demi", 10),
                           height=2, width=11, command=tab3).place(x=510, y=400)

    deleteTab()
    bisec = Tk()
    bisec.title("Bisección Gay")
    bisec.geometry("700x550")
    bisec.config(background="#272635")
    encabezado = Label(bisec, text="Introduce valores en la ecuación", fg="#A6A6A8", bg="#272635",
                       font=("Berlin Sans FB Demi", 20)).place(x=150, y=20)

    # Ecuación

    # dato de x2
    x2data = StringVar()
    valorx2 = Entry(width=2, textvariable=x2data, font=(
        "Berlin Sans FB Demi", 17)).place(x=250, y=90)
    x2 = Label(bisec, text="X +", fg="#A6A6A8", bg="#272635",
               font=("Berlin Sans FB Demi", 20)).place(x=280, y=89)
    # exponente de x2
    exp2data = StringVar()
    exponentex2 = Entry(width=2, textvariable=exp2data, font=(
        "Berlin Sans FB Demi", 10)).place(x=300, y=70)

    # dato de x1
    x1data = StringVar()
    valorx1 = Entry(width=2, textvariable=x1data, font=(
        "Berlin Sans FB Demi", 17)).place(x=325, y=89)
    x1 = Label(bisec, text="X +", fg="#A6A6A8", bg="#272635",
               font=("Berlin Sans FB Demi", 20)).place(x=355, y=89)
    # exponente de x1
    exp1data = StringVar()
    exponentex1 = Entry(width=2, textvariable=exp1data, font=(
        "Berlin Sans FB Demi", 10)).place(x=375, y=70)

    # dato de último término
    xdata = StringVar()
    valorx = Entry(width=2, textvariable=xdata, font=(
        "Berlin Sans FB Demi", 17)).place(x=400, y=89)
    x = Label(bisec, text="X", fg="#A6A6A8", bg="#272635",
              font=("Berlin Sans FB Demi", 20)).place(x=430, y=89)
    # exponente de x
    expdata = StringVar()
    exponentex = Entry(width=2, textvariable=expdata, font=(
        "Berlin Sans FB Demi", 10)).place(x=450, y=70)

    vergráfico = Button(bisec, text="Ver gráfico", fg="#FFFFFF", bg="#E4572E", font=("Berlin Sans FB Demi", 10),
                        height=2, width=11, command=calcGraf).place(x=310, y=140)


def tab1():
    encabezado = Label(bisec, text="¡Bienvenido!", fg="#A6A6A8", bg="#272635",
                       font=("Berlin Sans FB Demi", 50)).place(x=175, y=100)
    encabezado = Label(bisec, text="a", fg="#CECECE", bg="#272635",
                       font=("Berlin Sans FB Demi", 35)).place(x=335, y=170)
    encabezado = Label(bisec, text="Bisección Gay", fg="#B1E5F2", bg="#272635",
                       font=("Berlin Sans FB Demi", 25)).place(x=255, y=240)

    binary_button = Button(bisec, text="Empezar", fg="#FFFFFF", bg="#4D5393", font=("Berlin Sans FB Demi", 13),
                           height=2, width=11, command=tab2).place(x=295, y=340)

    """ingresar_numero = Label(bisec, text="Valor límite inferior", fg="#E4572E", bg="#29335C",
                            font=("Berlin Sans FB Demi", 10)).place(x=60, y=80)
    dato = StringVar()
    numero_entry = Entry(bisec, textvariable=dato,
                        justify="center").place(x=60, y=110) """


tab1()
bisec.resizable(False, False)
bisec.mainloop()
