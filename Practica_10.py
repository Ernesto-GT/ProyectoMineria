from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt
import csv
import nltk
from nltk.corpus import stopwords

def lectura():
    datos = ""
    info = ""
    palabras_eliminar = ["wa", "ni", "wo", "ga", "de"]
    
    with open('DataSetClean.csv', encoding="utf8") as f:
        reader = csv.reader(f)
        for row in reader:
            if(len(row) > 0):
                aux = 0
                for palabra in palabras_eliminar:
                    if(aux==0):
                        datos = row[1].replace(palabra,'')
                        aux = 1
                    else:
                        datos = datos.replace(palabra,"")
                info = info + datos
                datos = ""  
    return(info)


wordCloud = WordCloud().generate(lectura())

plt.imshow(wordCloud, interpolation='bilinear' )
plt.axis('off')

image = wordCloud.to_image()
image.save('NubePalabras_P10/Concat_Nombres.png')
image.show()
