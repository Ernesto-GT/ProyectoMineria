import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv('DataSetClean.csv')
    
def Puntaje_Fecha():
    Supernatural = datos.where((datos["Genres"] == 'Supernatural'))  
    Horror = datos.where((datos["Genres"] == 'Horror'))
    Gourmet = datos.where((datos["Genres"] == 'Gourmet'))
    Romance = datos.where((datos["Genres"] == 'Romance'))

    plt.scatter(Supernatural["Score"],Supernatural["Aired"], marker="+", s=30, color="blue")

    plt.scatter(Horror["Score"],Horror["Aired"], marker="1", s=30, color="green")

    plt.scatter(Gourmet["Score"],Gourmet["Aired"], marker=".", s=30, color="red")

    plt.scatter(Romance["Score"],Romance["Aired"], marker="x", s=25, color="orange")


    plt.ylabel("Fecha")
    plt.xlabel("Puntaje")
    plt.legend(bbox_to_anchor=(1,0.2))
    plt.savefig("Clasificacion_P7/Fecha-Puntaje.png")
    plt.show()



def Puntaje_Miembros():
    Supernatural = datos.where((datos["Genres"] == 'Supernatural'))  
    Horror = datos.where((datos["Genres"] == 'Horror'))
    Gourmet = datos.where((datos["Genres"] == 'Gourmet'))
    Romance = datos.where((datos["Genres"] == 'Romance'))

    plt.scatter(Supernatural["Score"],Supernatural["Members"], marker="+", s=30, color="blue")

    plt.scatter(Horror["Score"],Horror["Members"], marker="1", s=30, color="green")

    plt.scatter(Gourmet["Score"],Gourmet["Members"], marker=".", s=30, color="red")

    plt.scatter(Romance["Score"],Romance["Members"], marker="x", s=25, color="orange")


    plt.ylabel("Seguidores")
    plt.xlabel("Puntaje")
    plt.legend(bbox_to_anchor=(1,0.2))
    plt.savefig("Clasificacion_P7/Seguidores-Puntaje.png")
    plt.show()

Puntaje_Fecha()
Puntaje_Miembros()
