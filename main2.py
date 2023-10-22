import matplotlib.pyplot as plt
import random
import numpy as np

# Generar datos ficticios para PIB, inflación y desempleo
def generar_datos():
    periodos = ["Hora", "Día", "Mes", "Año"]
    tiempo = random.choice(periodos)
    tiempo_valores = {"Hora": 24, "Día": 30, "Mes": 12, "Año": 10}

    tiempo_escala = tiempo_valores[tiempo]
    
    # Asegurarnos de que x tenga la misma longitud que las series de tiempo
    x = np.arange(0, tiempo_escala)
    
    pib = np.cumsum(np.random.normal(100, 10, tiempo_escala))
    inflacion = np.random.normal(3, 1, tiempo_escala)
    desempleo = np.random.uniform(3, 10, tiempo_escala)

    return tiempo, x, pib, inflacion, desempleo

# Función para graficar los indicadores
def graficar_indicadores(tiempo, x, pib, inflacion, desempleo):
    tiempo_label = f"Tiempo ({tiempo})"
    
    plt.figure(figsize=(12, 6))

    plt.subplot(311)
    plt.plot(x, pib)
    plt.title(f"Comportamiento del PIB a lo largo del tiempo")
    plt.xlabel(tiempo_label)
    plt.ylabel("PIB")

    plt.subplot(312)
    plt.plot(x, inflacion)
    plt.title(f"Comportamiento de la Inflación a lo largo del tiempo")
    plt.xlabel(tiempo_label)
    plt.ylabel("Inflación")

    plt.subplot(313)
    plt.plot(x, desempleo)
    plt.title(f"Comportamiento del Desempleo a lo largo del tiempo")
    plt.xlabel(tiempo_label)
    plt.ylabel("Tasa de Desempleo")

    plt.tight_layout()
    plt.show()

# Ejecutar el programa
tiempo, x, pib, inflacion, desempleo = generar_datos()
graficar_indicadores(tiempo, x, pib, inflacion, desempleo)
