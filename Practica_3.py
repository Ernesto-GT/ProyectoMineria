import csv
import pandas as pd
#ED->Estadistica Descriptiva
#Analisis de la ED al relacionar cada uno de los Generos con la Puntuacion otorgada a cada serie
def EstadisticaPorGeneroYPuntajes():
    resultado = df.groupby('Genres')['Score'].agg(['count', 'mean', 'min', 'max', 'std', 'var'])
    resultado.columns = ['Total_Animes', 'Promedio', 'Puntaje_Minimo', 'Puntaje_Maximo', 'Desviacion_Estandar', 'Varianza']
    #print(resultado)
    resultado.to_csv('DataSet_Genero-Puntajes.csv')

#Analisis de la ED al relacionar cada uno de los Generos con la cantidad de Seguidores de la serie 
def EstadisticaPorGeneroYSeguidores():
    resultado = df.groupby('Genres')['Members'].agg(['sum', 'mean', 'min', 'max', 'std', 'var'])
    resultado.columns = ['Total_Seguidores', 'Promedio', 'Puntaje_Minimo', 'Puntaje_Maximo', 'Desviacion_Estandar', 'Varianza']
    #print(resultado)
    resultado.to_csv('DataSet_Genero-Seguidores.csv')

#Analisis de la ED al relacionar cada uno de los distintos Medios Audio-Visuales con la Puntuacion otorgada a la serie 
def EstadisticaPorTipoYPuntajes():
    resultado = df.groupby('Type')['Score'].agg(['count', 'mean', 'min', 'max', 'std', 'var'])
    resultado.columns = ['Total_Animes', 'Promedio', 'Puntaje_Minimo', 'Puntaje_Maximo', 'Desviacion_Estandar', 'Varianza']
    #print(resultado)
    resultado.to_csv('DataSet_Tipo-Puntajes.csv')

#Analisis de la ED respecto a los puntajes otorgados a las series, en base al año en que salieron
def EstadisticaPorFechaYPuntajes():
    resultado = df.groupby('Aired')['Score'].agg(['count', 'mean', 'min', 'max', 'std', 'var'])
    resultado.columns = ['Total_Animes', 'Promedio', 'Puntaje_Minimo', 'Puntaje_Maximo', 'Desviacion_Estandar', 'Varianza']
    #print(resultado)
    resultado.to_csv('DataSet_Fecha-Puntajes.csv')

#Analisis de la ED al relacionar cada uno de los Generos con la cantidad de Episodios que tiene cada titulo 
def EstadisticaPorGeneroYEpisodios():
    resultado = df.groupby('Genres')['Episodes'].agg(['count', 'mean', 'min', 'max', 'std', 'var'])
    resultado.columns = ['Total_Animes', 'Promedio', 'Puntaje_Minimo', 'Puntaje_Maximo', 'Desviacion_Estandar', 'Varianza']
    #print(resultado)
    resultado.to_csv('DataSet_Genero-Episodios.csv')

#Lectura de archivo csv
df = pd.read_csv('DataSetClean.csv')
#Ejecucios de las pruebas de Estadistica Descriptiva
EstadisticaPorGeneroYPuntajes()
EstadisticaPorGeneroYSeguidores()
EstadisticaPorTipoYPuntajes()
EstadisticaPorFechaYPuntajes()
EstadisticaPorGeneroYEpisodios()
