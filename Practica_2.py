import csv
import pandas as pd
datos = []

def asignar_Instancias():
    titulo = True
    n=0

    with open('DataSet.csv', encoding="utf8") as f:
        reader = csv.reader(f)
        for row in reader:
            if(titulo == True):
                datos.append(['anime_id','Name','Score','Genres','Type','Episodes','Aired','Source','Rank','Popularity','Members'])
                titulo = False
            elif(len(row) > 0):
                if(row[2] != 'UNKNOWN' and row[5] != 'UNKNOWN' and row[8] != 'UNKNOWN' and row[9] != 'UNKNOWN' and row[10] != 'UNKNOWN' and len(row[6]) > 10):
                    n += 1
                    posicion = row[6].find(',')
                    if(posicion > 0):
                        datos.append([n, row[1], row[2], row[3], row[4], row[5], int(row[6][(posicion + 2):(posicion + 6)]), row[7], row[8], row[9], row[10]])
                    
    return(datos)

df = pd.DataFrame(asignar_Instancias())
df.to_csv("DataSetClean.csv", index=False, header=False)
