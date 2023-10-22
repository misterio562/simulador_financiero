import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Función para actualizar el gráfico
def update_chart(canvas):
    x = np.arange(0, 2 * np.pi, 0.1)
    y = np.sin(x)
    ax.clear()
    ax.plot(x, y)
    ax.set_title("Gráfico")
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    
    

# Función para agregar datos de PIB al gráfico
def pib(canvas):
    # Dibujar la línea roja (simulando datos de PIB)
    x_pib = np.arange(0, 2 * np.pi, 0.1)
    y_pib = np.sin(x_pib) + np.random.rand(len(x_pib)) * 0.5  # Datos aleatorios para el PIB
    ax.plot(x_pib, y_pib, 'r', label='PIB')
    
    ax.legend()  # Mostrar la leyenda
    canvas.draw()

# Crear la ventana principal
root = tk.Tk()
root.title("Simulador Financiero")
root.geometry("900x700")
root.resizable(False, False)

# Crear un marco para la visualización del gráfico
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10, fill="both", expand=True)

# Crear un botón para actualizar el gráfico
update_button = ttk.Button(root, text="Actualizar Gráfico", command=lambda: update_chart(canvas))
update_button.pack(pady=10)

# Crear un botón para agregar datos de PIB al gráfico (línea roja)
btn_pib = ttk.Button(root, text="PIB", command=lambda: pib(canvas))
btn_pib.place(x=100, y=650)

# Crear un gráfico inicial
fig, ax = plt.subplots(figsize=(5, 4))
update_chart(FigureCanvasTkAgg(fig, master=frame))  # Llamar a la función para mostrar el gráfico inicial

# Integrar el gráfico de Matplotlib en la interfaz de usuario de tkinter
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Iniciar la aplicación
root.mainloop()
