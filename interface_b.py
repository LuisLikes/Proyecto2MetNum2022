from doctest import master
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
        x = np.linspace(-10, 10, 100)
        y = -0.5*x**2+2.5*x+4.5
        fig = plt.figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax = plt.plot(x, y, 'r')
        ax = FigureCanvasTkAgg(fig, master=bisec)
        ax.get_tk_widget().place(x=30, y=200)

    deleteTab()
    bisec = Tk()
    bisec.title("Bisección Gay")
    bisec.geometry("700x550")
    bisec.config(background="#272635")
    encabezado = Label(bisec, text="Introduce valores en la ecuación", fg="#A6A6A8", bg="#272635",
                       font=("Berlin Sans FB Demi", 20)).place(x=150, y=20)  # 50

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
    x1data = Label(bisec, text="X +", fg="#A6A6A8", bg="#272635",
                   font=("Berlin Sans FB Demi", 20)).place(x=355, y=89)
    # exponente de x1
    exp1data = StringVar()
    exponentex1 = Entry(width=2, textvariable=exp1data, font=(
        "Berlin Sans FB Demi", 10)).place(x=375, y=70)

    # dato de último término
    valor = Entry(width=2, font=(
        "Berlin Sans FB Demi", 17)).place(x=400, y=89)
    xdata = Label(bisec, text="X", fg="#A6A6A8", bg="#272635",
                  font=("Berlin Sans FB Demi", 20)).place(x=430, y=89)
    # exponente de x
    expdata = StringVar()
    exponentex = Entry(width=2, textvariable=exp1data, font=(
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
