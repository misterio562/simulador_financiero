import numpy as np
import matplotlib.pyplot as plt
x=np.array([2021,2022])
y=np.array([269.121, 326.356])

def fx (x1, coef):
    fx = 0
    n = len(coef) - 1
    for p in coef:
        fx = fx + p*x1**n
        n = n - 1
    return fx

annos_prediccion = [2023, 2024, 2025]

coef = np.polyfit(x,y,7)

for anno in annos_prediccion:
    p = np.polyval(coef, anno)

    print(f"para el año {anno} la predicción es {p}")
    x1 = np.linspace(2021, max(annos_prediccion) + 1, 1000)
    y1 = fx(x1, coef) # funcion
    plt.figure(figsize=[20,10])
    plt.title("PIB vs año. Para grado: " + str(7))

    plt.scatter(x,y,s=120,c='blueviolet')
    plt.plot(x1,y1,"--",linewidth=3,color='orange')
    plt.scatter(annos_prediccion,[np.polyval(coef, anno) for anno in annos_prediccion],s=200,c='red')
    plt.yticks(range(200,600,20))
    plt.grid("on")
    ax=plt.gca()
    ax.set_xlabel("$Años$")
    ax.set_ylabel("$PIB$")
    #plt.savefig("img" + str(i)+".jpg", dpi=600)
    plt.show()