import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

df = pd.read_csv('DataSetClean.csv')

def anova(df_aux: pd.DataFrame, str_ols: str):
    modl = ols(str_ols, data=df_aux).fit()
    anova_df = sm.stats.anova_lm(modl, typ=2)
    if anova_df["PR(>F)"][0] < 0.005:
        print("Hay diferencias")
        print(anova_df)
    else:
        print("No hay diferencias")

def anova_1():
    df_by_type = df.groupby(["Aired", "Genres"]).agg({"Score": "mean"})
    df_by_type.reset_index(inplace=True)
    df_aux = df_by_type.rename(columns={"Aired": "Estreno"})
    anova(df_aux, "Score ~ C(Estreno) + C(Genres)")

anova_1()