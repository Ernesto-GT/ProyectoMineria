import pandas as pd
from scipy.stats import f_oneway
import statsmodels.api as sm
from statsmodels.formula.api import ols

df = pd.read_csv('DataSetClean.csv')

#------------------------------ ANOVA Forma - 1 ------------------------------------------------------------#
#Comprobacion
def comprobar(df_aux: pd.DataFrame, str_ols: str):
    modl = ols(str_ols, data=df_aux).fit()
    anova_df = sm.stats.anova_lm(modl, typ=2)
    if anova_df["PR(>F)"][0] < 0.005:
        print("Hay diferencias")
        print(anova_df)
    else:
        print("No hay diferencias")

#Comparando los promedios de puntaje, agrupando por Fecha y Generos 
def anova_1():
    df_by_type = df.groupby(["Aired", "Genres"]).agg({"Score": "mean"})
    df_by_type.reset_index(inplace=True)
    df_aux = df_by_type.rename(columns={"Aired": "Estreno", "Genres": "Generos"})
    comprobar(df_aux, "Score ~ Estreno + Generos")

#Comparando los promedios de puntaje, agrupando por Origen y Generos 
def anova_2():
    df_by_type = df.groupby(["Source", "Genres"]).agg({"Score": "mean"})
    df_by_type.reset_index(inplace=True)
    df_aux = df_by_type.rename(columns={"Source": "Tipos","Genres": "Generos"})
    comprobar(df_aux, "Score ~ Tipos + Generos")

#------------------------------ ANOVA Forma - 2 ------------------------------------------------------------#
#Comprobacion
def comprobar_2(resultado):
    if resultado.pvalue < 0.05:
        print("Hay diferencias significativas entre los grupos.\n")
    else:
        print("No hay diferencias significativas entre los grupos.\n")

#Nota:Estas pruebas se hicieron en base a las Graficas de Bigote hechas en la practica pasada, buscando las semejanzas en varianza

#Generos - Puntaje Promedio
def anova_3():
    grupos = df.groupby('Genres')['Score'].apply(list)
    #Comparando Generos "Sobrenatual y Girls Love"
    resultado = f_oneway(grupos[16], grupos[17])
    print( " \n Comparando Generos 'Sobrenatual y Girls Love':" )
    print(resultado)
    comprobar_2(resultado)
    #Comparando Generos "Romance y Gourmet"
    resultado2 = f_oneway(grupos[14], grupos[18])
    print(" \n Comparando Generos 'Romance y Gourmet':" )
    print(resultado2)
    comprobar_2(resultado2)
    #Comparando Generos "Action y Adventure"
    resultado3 = f_oneway(grupos[0], grupos[1])
    print(" \n Comparando Generos 'Action y Adventure':" )
    print(resultado3)
    comprobar_2(resultado3)

#Origen - Puntaje Promedio
def anova_4():
    grupos = df.groupby('Source')['Score'].apply(list)
    #Comparando Origenes "Manga y Novel"
    resultado = f_oneway(grupos[1], grupos[6])
    print( " \n Comparando Generos 'Manga y Novel':" )
    print(resultado)
    comprobar_2(resultado)
    #Comparando Origenes "Indeterminado y Picture Book"
    resultado2 = f_oneway(grupos[8], grupos[9])
    print(" \n Comparando Generos 'Otros y Picture Book':" )
    print(resultado2)
    comprobar_2(resultado2)
    #Comparando Generos "Original y Manga"
    resultado3 = f_oneway(grupos[0], grupos[1])
    print(" \n Comparando Generos 'Original y Manga':" )
    print(resultado3)
    comprobar_2(resultado3)

#Tipo de Visualizacion - Puntaje Promedio
def anova_5():
    grupos = df.groupby('Type')['Score'].apply(list)
    #Comparando Tipo "OVA y Special"
    resultado = f_oneway(grupos[2], grupos[3])
    print( " \n Comparando Tipos 'OVA y Special':" )
    print(resultado)
    comprobar_2(resultado)
    #Comparando Origenes "OVA y ONA"
    resultado2 = f_oneway(grupos[2], grupos[4])
    print(" \n Comparando Tipos 'OVA y ONA':" )
    print(resultado2)
    comprobar_2(resultado2)
    #Comparando Generos "TV y Movie"
    resultado3 = f_oneway(grupos[0], grupos[1])
    print(" \n Comparando Tipos 'TV y Movie':" )
    print(resultado3)
    comprobar_2(resultado3)

#Ejecuciones de los distintos ANOVA's creados (Recomendacion: ejecutar uno a la vez)
#anova_1()
#anova_2()
#anova_3()
anova_4()
anova_5()