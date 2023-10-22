import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Función para graficar


def graficar():
    # Cargar los datos desde el archivo Excel
    archivo_excel = 'pib.xlsx'
    df = pd.read_excel(archivo_excel)

    # Extraer las columnas de años y valores en dólares
    años = df['Año']
    valores = df['PIB']

    # Cargar los datos de la deuda desde el archivo Excel
    archivo_deuda = 'deuda.xlsx'
    df_deuda = pd.read_excel(archivo_deuda)

    # Extraer las columnas de años y valores de la deuda
    años_deuda = df_deuda['Año']
    valores_deuda = df_deuda['Deuda']

    # Crear el gráfico de línea
    plt.figure(figsize=(6, 4))  # Ajusta el tamaño del gráfico si es necesario
    plt.plot(años, valores, marker='o', linestyle='-', color='b', label='PIB')

    for i in range(len(años)):
        plt.text(años[i], valores[i], str(valores[i]), ha='left', va='bottom')

     # Gráfico de Deuda en rojo
    plt.plot(años_deuda, valores_deuda, marker='o',
             linestyle='-', color='r', label='Deuda')

    for i in range(len(años_deuda)):
        plt.text(años_deuda[i], valores_deuda[i], str(
            valores_deuda[i]), ha="left", va="bottom")

    plt.title('Gráfica indicadora')
    plt.xlabel('Año')
    plt.ylabel('Valor en millones dólares')
    plt.grid(True)
    plt.legend()

    # Crear una ventana de tkinter
    root = Tk()
    root.title('Gráfico del PIB en Dólares')
    root.geometry("800x700")

    # Agregar el gráfico a la ventana tkinter
    canvas = FigureCanvasTkAgg(plt.gcf(), master=root)
    canvas.get_tk_widget().pack()
    canvas.draw()

    plt.xticks(años)

    # Iniciar el bucle principal de tkinter
    root.mainloop()


# Llamar a la función para mostrar el gráfico
graficar()
