import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np  
import os


# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('DataSetClean.csv')

def Kmeans_1():
    top = pd.read_csv('DataSetClean.csv').query('anime_id <= 1000')
    top_P = top[["Score", "Popularity"]]

    SumaDistancias = []

    for k in range(1,10):
        kmeans = KMeans(n_clusters = k, random_state=0, n_init=5)
        kmeans.fit_predict(top_P)
        SumaDistancias.append(kmeans.inertia_)        
        plt.scatter(x=top_P["Score"], y=top_P["Popularity"], c=kmeans.labels_, s=5)
        plt.xlabel("Puntuacion General")
        plt.ylabel("Posicion en cuanto a Popularidad")
        plt.savefig(os.path.join('Kmeans_P8/Score_x_Popularity/','Kmeans con K ='+str(k)))
        plt.clf()
        
    # Graficar la suma de cuadrados de distancias en función de n_clusters
    plt.plot(range(1,10), SumaDistancias, 'bx-')
    plt.xlabel('Número de Clusters (k)')
    plt.ylabel('Suma de Cuadrados de Distancias')
    plt.title('Método del Codo para Determinar k')
    plt.savefig(os.path.join('Kmeans_P8/Score_x_Popularity/', 'Metodo del codo de Kmeans'))

def Kmeans_2():
    top = pd.read_csv('DataSetClean.csv').query('anime_id <= 2000')
    top_P = top[["Rank", "Popularity"]]

    SumaDistancias = []

    for k in range(1,10):
        kmeans = KMeans(n_clusters = k, random_state=0, n_init=5)
        kmeans.fit_predict(top_P)
        SumaDistancias.append(kmeans.inertia_)        
        plt.scatter(x=top_P["Rank"], y=top_P["Popularity"], c=kmeans.labels_, s=5)
        plt.xlabel("Posicion en cuanto a Puntaje")
        plt.ylabel("Posicion en cuanto a Popularidad")
        plt.savefig(os.path.join('Kmeans_P8/Rank_x_Popularity/','Kmeans con K ='+str(k)))
        plt.clf()
        
    # Graficar la suma de cuadrados de distancias en función de n_clusters
    plt.plot(range(1,10), SumaDistancias, 'bx-')
    plt.xlabel('Número de Clusters (k)')
    plt.ylabel('Suma de Cuadrados de Distancias')
    plt.title('Método del Codo para Determinar k')
    plt.savefig(os.path.join('Kmeans_P8/Rank_x_Popularity/', 'Metodo del codo de Kmeans'))

Kmeans_1()
Kmeans_2()