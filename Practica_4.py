import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('DataSetClean.csv')

#Grafica de Bigote, tomando los Puntajes otorgados a cada serie, agrupando por Genero
sns.boxplot(x="Score", y="Genres", data=df)
plt.savefig(f"Graficas_P4/GBigote_Puntajes-Genero.png")
#plt.show()
plt.gcf().clear()

#Grafica de Bigote, tomando los Puntajes otorgados a cada serie, agrupando por Tipo de Visualizacion 
sns.boxplot(x="Score", y="Source", data=df)
plt.savefig(f"Graficas_P4/GBigote_Puntajes-Tipos.png")
#plt.show()
plt.gcf().clear()

#Grafica de Pastel, tomando en cuenta la catidad de Seguidores que tiene cada Tipo de Visualizacion
df_v = df.groupby('Type')['Members'].sum()
plot = df_v.plot.pie(y='Type', figsize=(10,10), autopct="%1.0f%%")
resultado = df.groupby('Type')['Members'].sum()
print(resultado)
plt.savefig(f"Graficas_P4/GPastel_Seguidores-Tipos.png")
#plt.show()
plt.gcf().clear()