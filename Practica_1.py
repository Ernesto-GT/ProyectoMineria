import pandas as pd
from tabulate import tabulate 
import requests
import io

def get_csv_from_url(url: str) -> pd.DataFrame:

    req = requests.get(url).content
    return pd.read_csv(io.StringIO(req.decode('utf-8')))


df = get_csv_from_url("https://raw.githubusercontent.com/AldoSantellano/MineriaBases/main/Anime/DataSet.csv")
df.to_csv("DataSet.csv", index=False) 