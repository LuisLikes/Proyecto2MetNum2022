from typing_extensions import Self
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
from matplotlib.figure import Figure
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
plt.use('TkAgg')
# Funciones

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
        # 100 linearly spaced numbers
        x = np.linspace(-5, 5, 100)

        # the function, which is y = x^2 here
        y = x**3+x**2+4

        # setting the axes at the centre
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')

        # plot the function
        plt.plot(x, y, 'r')

        graph = Figure(figsize=(6, 4), dpi=100)
        graph_canvas = FigureCanvasTkAgg(graph, self)
        NavigationToolbar2Tk(graph_canvas, self)
        axes = graph.add_subplot()
        graph_canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    deleteTab()
    bisec = Tk()
    bisec.title("Bisección Gay")
    bisec.geometry("700x550")
    bisec.config(background="#272635")
    encabezado = Label(bisec, text="Introduce valores en la ecuación", fg="#A6A6A8", bg="#272635",
                       font=("Berlin Sans FB Demi", 20)).place(x=150, y=50)

    # Ecuación

    # dato de x2
    x2data = StringVar()
    valorx2 = Entry(width=2, textvariable=x2data, font=(
        "Berlin Sans FB Demi", 17)).place(x=250, y=120)
    x2 = Label(bisec, text="X +", fg="#A6A6A8", bg="#272635",
               font=("Berlin Sans FB Demi", 20)).place(x=280, y=119)
    # exponente de x2
    exp2data = StringVar()
    exponentex2 = Entry(width=2, textvariable=exp2data, font=(
        "Berlin Sans FB Demi", 10)).place(x=300, y=100)

    # dato de x1
    x1data = StringVar()
    valorx1 = Entry(width=2, textvariable=x1data, font=(
        "Berlin Sans FB Demi", 17)).place(x=325, y=120)
    x1data = Label(bisec, text="X +", fg="#A6A6A8", bg="#272635",
                   font=("Berlin Sans FB Demi", 20)).place(x=355, y=119)
    # exponente de x1
    exp1data = StringVar()
    exponentex1 = Entry(width=2, textvariable=exp1data, font=(
        "Berlin Sans FB Demi", 10)).place(x=375, y=100)

    # dato de último término
    valor = Entry(width=2, font=(
        "Berlin Sans FB Demi", 17)).place(x=400, y=119)
    xdata = Label(bisec, text="X", fg="#A6A6A8", bg="#272635",
                  font=("Berlin Sans FB Demi", 20)).place(x=430, y=119)
    # exponente de x
    expdata = StringVar()
    exponentex = Entry(width=2, textvariable=exp1data, font=(
        "Berlin Sans FB Demi", 10)).place(x=450, y=100)

    vergráfico = Button(bisec, text="Ver gráfico", fg="#FFFFFF", bg="#E4572E", font=("Berlin Sans FB Demi", 10),
                        height=2, width=11, command=calcGraf).place(x=310, y=170)


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
