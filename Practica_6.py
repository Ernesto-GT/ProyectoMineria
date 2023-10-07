import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

datos = pd.read_csv('DataSetClean.csv')
datos = datos.where(datos["Type"] == 'Movie')   


# Usa seaborn para crear un gráfico de dispersión con la línea de regresión
sns.lmplot(x='Aired', y='Score', data=datos)
# Muestra el gráfico
plt.xlabel('Puntaje')
plt.ylabel('Fecha Emision')
plt.title('Regresión Lineal: Puntaje vs Fecha Emision')
plt.show()
#plt.savefig('RegresionLineal.png')
plt.close()