import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

class Macro:

    def __init__(self, frame_main):
        self.frame_main = frame_main

    def get_content(self):
        # Obtener la ruta al archivo pib.xlsx en la raíz del proyecto
        root_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))  # Retroceder tres niveles hasta llegar a la raíz del proyecto        excel_file_path = os.path.join(root_path, "pib.xlsx")
        excel_file_path = os.path.join(root_path, "pib.xlsx")

        # Cargar los datos desde el archivo Excel
        df = pd.read_excel(excel_file_path)

        #Obtener los valores de las columnas "Año" y "PIB"
        x = df["Año"].values
        y = df["PIB"].values
        
        annos_prediccion = [2023, 2024, 2025] # Años que se quieren predecir

        # Ajuste polinómico
        coef = np.polyfit(x, y, 2) # ax^2 + bx + c    a  (x, y)
        x1 = np.linspace(2021, max(annos_prediccion), 1000)
        y1 = fx(x1, coef)  # función

        # Agregar los años predichos a los datos
        x_prediccion = np.concatenate((x, annos_prediccion))
        y_prediccion = np.concatenate((y, [np.polyval(coef, anno) for anno in annos_prediccion]))

        # Crear una figura de Matplotlib
        fig = plt.figure(figsize=(6, 8))

        # Crear la primera gráfica en la parte superior
        ax1 = fig.add_subplot(211)
        ax1.plot(x_prediccion, y_prediccion, marker='o', label="PIB")
        plt.plot(x1,y1,"--",linewidth=3,color='red', label="Predicción")
        





        # Cargar los datos de "deuda.xlsx"
        deuda_file_path = os.path.join(root_path, "deuda.xlsx")
        deuda_df = pd.read_excel(deuda_file_path)
        deuda_x = deuda_df["Año"].values
        deuda_y = deuda_df["Deuda"].values

        # Ajuste polinómico
        coef_deuda = np.polyfit(deuda_x, deuda_y, 2) # ax^2 + bx + c    a  (x, y)
        deuda_x1 = np.linspace(2021, max(annos_prediccion), 1000)
        deuda_y1 = fx(deuda_x1, coef_deuda)  # función

        # Agregar los años predichos a los datos
        x_prediccion_deuda = np.concatenate((deuda_x, annos_prediccion))
        y_prediccion_deuda = np.concatenate((deuda_y, [np.polyval(coef_deuda, anno) for anno in annos_prediccion]))

        # Agregar una línea amarilla para los datos de deuda
        ax1.plot(x_prediccion_deuda, y_prediccion_deuda, color='yellow', marker='o', label="Deuda")
        plt.plot(deuda_x1,deuda_y1,"--",linewidth=3,color='red')



        ax1.set_title("Gráfica PIB y Deuda")
        ax1.legend()

         # Personalizar el eje x para mostrar años como enteros
        ax1.xaxis.set_major_locator(plt.MaxNLocator(integer=True))
        ax1.set_xticks(x_prediccion)
        ax1.set_ylabel("M€")
        ax1.set_xlabel("Año")

        # Anotar los valores al lado de los puntos en la gráfica pib
        for i, txt in enumerate(y_prediccion):
            ax1.annotate("{:.2f}".format(txt), (x_prediccion[i], y_prediccion[i]), textcoords="offset points", xytext=(0,10), ha='center')

        for i, txt in enumerate(y_prediccion_deuda): # Deuda
            ax1.annotate("{:.2f}".format(txt), (x_prediccion_deuda[i], y_prediccion_deuda[i]), textcoords="offset points", xytext=(0,10), ha='center')





        # Cargar los datos de "deuda.xlsx"
        inflacion_file_path = os.path.join(root_path, "inflacion.xlsx")
        inflacion_df = pd.read_excel(inflacion_file_path)
        inflacion_x = inflacion_df["Año"].values
        inflacion_y = inflacion_df["Inflacion"].values

        print(inflacion_x, inflacion_y)

        # Ajuste polinómico
        coef_inflacion = np.polyfit(inflacion_x, inflacion_y, 2) # ax^2 + bx + c    a  (x, y)
        inflacion_x1 = np.linspace(2021, max(annos_prediccion), 1000)
        inflacion_y1 = fx(inflacion_x1, coef_inflacion)  # función

        # Agregar los años predichos a los datos
        x_prediccion_inflacion = np.concatenate((inflacion_x, annos_prediccion))
        y_prediccion_inflacion = np.concatenate((inflacion_y, [np.polyval(coef_inflacion, anno) for anno in annos_prediccion]))

        # Agregar una línea amarilla para los datos de deuda
        ax2 = fig.add_subplot(212)
        ax2.plot(x_prediccion_inflacion, y_prediccion_inflacion, color='green', marker='o', label="Inflacion")
        plt.plot(inflacion_x1,inflacion_y1,"--",linewidth=3,color='red')
        plt.plot(inflacion_x1,inflacion_y1,"--",linewidth=3,color='red', label="Predicción")


        # Crear la segunda gráfica en la parte inferior (puedes personalizarla según tus necesidades)
        
        # ax2.plot([1, 2, 3, 4], [4, 2, 3, 1])  # Ejemplo de datos y gráfico
        ax2.set_title("Gráfica Inflación")
        ax2.legend()

        # Ajustar la posición de la segunda gráfica
        ax2.set_position([0.1, 0.1, 0.8, 0.3])  # [left, bottom, width, height]
         # Personalizar el eje x para mostrar años como enteros
        ax2.xaxis.set_major_locator(plt.MaxNLocator(integer=True))
        ax2.set_xticks(x_prediccion_inflacion)
        ax2.set_ylabel("Inflacion %")
        ax2.set_xlabel("Año")

        for i, txt in enumerate(y_prediccion_inflacion): # Deuda
            ax2.annotate("{:.2f}".format(txt), (x_prediccion_inflacion[i], y_prediccion_inflacion[i]), textcoords="offset points", xytext=(0,10), ha='center')


        # Crear un lienzo de Matplotlib
        canvas = FigureCanvasTkAgg(fig, master=self.frame_main)
        canvas_widget = canvas.get_tk_widget()

        return canvas_widget

def fx(x1, coef):
    fx = 0
    n = len(coef) - 1
    for p in coef:
        fx = fx + p * x1**n
        n = n - 1
    return fx
