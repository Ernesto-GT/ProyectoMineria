import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
import numbers
import pandas as pd
from tabulate import tabulate
from typing import Tuple, Dict
import numpy as np

df = pd.read_csv("DataSetClean.csv")

def Forecasting(genre, tipo, value, title):
    cond1 = df[tipo] ==  genre
    cond2 = df["Aired"] > 1917
    cond3 = df["Aired"] < 2023
    dfGroup = df.where(cond1 & cond2 & cond3)
    db = dfGroup.groupby("Aired").agg({value: "mean"})
    db.reset_index(inplace=True)

    model = smf.ols(value + ' ~ ' + "Aired", db)
    results = model.fit()
    alpha = .05
    predictions = results.get_prediction(db).summary_frame(alpha)


    plt.scatter(db["Aired"], db[value], s=10)
    plt.plot(db["Aired"], predictions['mean'], color='green')
    plt.fill_between(db["Aired"], predictions['obs_ci_lower'], predictions['obs_ci_upper'], alpha=.1, color='green')
    plt.xlabel('Year')
    plt.ylabel(value)
    plt.title('Forecasting ' + title)
    plt.savefig("Forecasting_P9/"+ title +".png")
    #plt.show()
    plt.close()
    plt.clf()
#Por Generos 
Forecasting("Action", "Genres", "Score", "Action_Score")
Forecasting("Comedy", "Genres", "Score", "Comedy_Score")
Forecasting("Sports", "Genres", "Episodes", "Sports_Episodes")

#Por Origen
Forecasting("Manga", "Source", "Score", "Manga_Score")
Forecasting("Original", "Source", "Score", "Original_Score")
Forecasting("Novel", "Source", "Score", "Novel_Score")

#Por Tipo de Visualización 
Forecasting("TV", "Type", "Episodes", "TV_Episodes")
Forecasting("TV", "Type", "Members", "TV_Members")
Forecasting("TV", "Type", "Score", "TV_Score")
Forecasting("Movie", "Type", "Score", "Movie_Score")
Forecasting("Movie", "Type", "Members", "Movie_Members")
Forecasting("OVA", "Type", "Members", "OVA_Members")