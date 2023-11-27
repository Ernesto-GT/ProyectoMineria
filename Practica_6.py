import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

datos = pd.read_csv('DataSetClean.csv')

def RL_MoviesAdventure():
    datos2 = datos.where((datos["Type"] == 'Movie') & (datos["Genres"] == 'Adventure'))  

    # Gráfico de dispersión con la línea de regresión
    sns.lmplot(x='Aired', y='Score', data=datos2, line_kws={'color': 'red'})
    prom = datos2['Score'].mean()
    # Promedio
    plt.axhline(y=prom, xmin=0.01, xmax=0.99, color="green")

    # Muestra el gráfico
    plt.xlabel('Puntaje')
    plt.ylabel('Fecha Emision')
    plt.title('Regresión Lineal: Puntaje vs Fecha Emision \n (Peliculas de Aventura)')
    fig = plt.gcf()
    fig.set_size_inches(10, 10)
    plt.savefig("RegresionLineal_P6/Movies-Adventure_Fecha-Puntaje.png")
    #plt.show()
    plt.close()

def RL_MangaSports():
    datos2 = datos.where((datos["Source"] == 'Manga') & (datos["Genres"] == 'Sports'))  

    # Gráfico de dispersión con la línea de regresión
    sns.lmplot(x='Aired', y='Score', data=datos2, line_kws={'color': 'red'})
    prom = datos2['Score'].mean()
    # Promedio
    plt.axhline(y=prom, xmin=0.01, xmax=0.99, color="green")

    # Muestra el gráfico
    plt.xlabel('Miembros')
    plt.ylabel('Fecha Emision')
    plt.title('Regresión Lineal: Puntajes vs Fecha Emision \n (Series de Deportes basadas en Manga)')
    fig = plt.gcf()
    fig.set_size_inches(10, 10)
    plt.savefig("RegresionLineal_P6/Manga-Deportes_Fecha-Puntaje.png")
    #plt.show()
    plt.close()

RL_MoviesAdventure()
RL_MangaSports()






