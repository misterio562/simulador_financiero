import pandas as pd
import matplotlib.pyplot as plt

class PIB():
    def __init__(self, frame):
        self.widget(frame)

    def widget(self):
        archivo_excel = 'pib.xlsx'
        df = pd.read_excel(archivo_excel)

        años = df['Año']
        valores = df['PIB']

        plt.figure(figsize=(6, 4))
        plt.plot(años, valores, 'o', linestyle='-', color='b', label='PIB')

        for i in range(len(años)):
            plt.text(años[i], valores[i], ha='left', va='bottom')

        plt.title('Gráfica indicadora')
        plt.xlabel('Año')
        plt.ylabel('Valor en millones dólares')
        plt.grid(True)
        plt.legend()

        plt.xticks(años)    



        