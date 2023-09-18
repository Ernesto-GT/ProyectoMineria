import csv
import pandas as pd

#Cantidad de series registradas agrupadas por genero
def Cantidad_Genero():
    resultado = df.groupby('Genres')['Name'].count()
    print(resultado)
#Promedio de puntaje de todas las series agrupadas por por genero 
def Puntaje_Promedio_Genero():
    resultado = df.groupby('Genres')['Score'].mean()
    print(resultado)
#Cantidad de seguidores registrados para cada tipo de anime
def Cantidad_Miembros_Tipo():
    resultado = df.groupby('Type')['Members'].sum()
    print(resultado)
#

def Min_Max_Puntaje():
    resultado = df['Score'].min()
    resultado2 = df.groupby('Name')['Score'].max()
    print(resultado)

df = pd.read_csv('DataSetClean.csv')
#Cantidad_Genero()
#Puntaje_Promedio_Genero()
#Cantidad_Miembros_Tipo()
Min_Max_Puntaje()
