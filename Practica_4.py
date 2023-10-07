import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('DataSetClean.csv')

#Grafica de Bigote, tomando los Puntajes otorgados a cada serie, agrupando por Genero
sns.boxplot(x="Score", y="Genres", data=df)
plt.suptitle("Promedio de Puntajes Agrupados por Genero", fontweight="bold")
plt.savefig(f"Graficas_P4/GBigote_Puntajes-Genero.png")
#plt.show()
plt.gcf().clear()

#Grafica de Bigote, tomando los Puntajes otorgados a cada serie, agrupando por Origen de la Serie
sns.boxplot(x="Score", y="Source", data=df)
plt.suptitle("Promedio de Puntajes Agrupados por Tipo de Origen", fontweight="bold")
plt.savefig(f"Graficas_P4/GBigote_Puntajes-Origen.png")
#plt.show()
plt.gcf().clear()

#Grafica de Bigote, tomando los Puntajes otorgados a cada serie, agrupando por Tipo de Visualizacion
sns.boxplot(x="Score", y="Type", data=df)
plt.suptitle("Promedio de Puntaje Agrupados por Tipo de Visualizacion", fontweight="bold")
plt.savefig(f"Graficas_P4/GBigote_Puntajes-Tipos.png")
#plt.show()
plt.gcf().clear()

desfase = (0, 0, 0, 0, 0.1)
#Grafica de Pastel, tomando en cuenta la catidad de Seguidores que tiene cada Tipo de Visualizacion
df_v = df.groupby('Type')['Members'].sum()
plot = df_v.plot.pie(y='Type', figsize=(10,10), autopct="%1.0f%%", startangle=140, explode=desfase)
plt.suptitle("Cantidad de Seguidores Registrados Agrupados por Tipo de Visualizacion", fontweight="bold")
plt.axis('equal')
plt.savefig(f"Graficas_P4/GPastel_Seguidores-Tipos.png")
#plt.show()
plt.gcf().clear()

#Grafica de Pastel, tomando en cuenta la catidad de Series que tiene cada Tipo de Visualizacion
df_v = df.groupby('Type')['anime_id'].count()
plot = df_v.plot.pie(y='Type', figsize=(10,10), autopct="%1.0f%%", startangle=100, explode=desfase)
plt.suptitle("Cantidad de Series Registradas Agrupadas por Tipo de Visualizacion", fontweight="bold")
plt.axis('equal')
plt.savefig(f"Graficas_P4/GPastel_Series-Tipos.png")
#plt.show()
plt.gcf().clear()

#Graficas conciderando el Top 100 del ranked 
top = pd.read_csv('DataSetClean.csv').query('Rank <= 100')

#Grafica de Bigote, tomando los Puntajes otorgados a cada serie, agrupando por Genero
sns.boxplot(x="Score", y="Genres", data=top)
plt.suptitle("Promedio de Puntaje Agrupados por Genero", fontweight="bold")
plt.savefig(f"Graficas_P4/GBigote_Puntajes-Generos_Top100.png")
#plt.show()
plt.gcf().clear()

#Grafica de Bigote, tomando los Puntajes otorgados a cada serie, agrupando por Tipo de Visualizacion
sns.boxplot(x="Score", y="Type", data=top)
plt.suptitle("Promedio de Puntaje Agrupados por Tipo de Visualizacion", fontweight="bold")
plt.savefig(f"Graficas_P4/GBigote_Puntajes-Tipos_Top100.png")
#plt.show()
plt.gcf().clear()

#Grafica de Pastel, tomando en cuenta la catidad de Series que tiene cada Tipo de Visualizacion
df_v = top.groupby('Genres')['anime_id'].count()
plot = df_v.plot.pie(y='Genres', figsize=(10,10), autopct="%1.0f%%", startangle=100)
plt.suptitle("Cantidad de Series Registradas Agrupadas por Genero", fontweight="bold")
plt.axis('equal')
plt.savefig(f"Graficas_P4/GPastel_Series-Generos_Top100.png")
#plt.show()
plt.gcf().clear()

#Grafica de Pastel, tomando en cuenta la catidad de Series que tiene cada Tipo de Visualizacion
df_v = top.groupby('Type')['anime_id'].count()
plot = df_v.plot.pie(y='Type', figsize=(10,10), autopct="%1.0f%%", startangle=100, explode=desfase)
plt.suptitle("Cantidad de Series Registradas Agrupadas por Tipo de Visualizacion", fontweight="bold")
plt.axis('equal')
plt.savefig(f"Graficas_P4/GPastel_Series-Tipos_Top100.png")
#plt.show()
plt.gcf().clear()
