import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
import numbers
import pandas as pd
from tabulate import tabulate
from typing import Tuple, Dict
import numpy as np

df = pd.read_csv("DataSetClean.csv")

def Forecasting(genre, inter, value, title):
    cond1 = df["Genres"] ==  genre
    cond2 = df[inter] > 1917
    cond3 = df[inter] < 2023
    dfGroup = df.where(cond1 & cond2 & cond3)
    db = dfGroup.groupby(inter).agg({value: "mean"})
    db.reset_index(inplace=True)

    model = smf.ols(value + ' ~ ' + inter, db)
    results = model.fit()
    alpha = .05
    predictions = results.get_prediction(db).summary_frame(alpha)


    plt.scatter(db[inter], db[value], s=10)
    plt.plot(db[inter], predictions['mean'], color='green')
    plt.fill_between(db[inter], predictions['obs_ci_lower'], predictions['obs_ci_upper'], alpha=.1, color='green')
    plt.xlabel('Año')
    plt.ylabel('Puntuacion Promedio')
    plt.savefig("Forecasting_P9/"+ title +".png")
    plt.show()
    plt.close()
    plt.clf()

Forecasting("Action", "Aired", "Score", "Action_Score")
Forecasting("Comedy", "Aired", "Score", "Comedy_Score")
Forecasting("Sports", "Aired", "Episodes", "Sports_Episodes")

