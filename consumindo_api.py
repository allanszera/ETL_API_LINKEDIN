import requests
import pandas as pd
import os
from pyodbc import drivers
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
api_url = os.getenv("API_URL")
api_host = os.getenv("API_HOST")

#link da API

url = f"https://linkedin-data-api.p.rapidapi.com/search-jobs?keywords=etl&locationId=104413988&datePosted=anyTime&sort=mostRelevant"

headers = {
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": api_host
}

response = requests.get(url, headers=headers)

dados = response.json()

df = pd.DataFrame([dados])


lista_de_dados = df['data'].iloc[0]

df_expanded = pd.json_normalize(lista_de_dados)


#SALVAR OS DADOS NO SQLSERVER
data_base = os.getenv("DATA_BASE")

server = r'DESKTOP-1KEA5IJ'
database = data_base
driver = 'ODBC Driver 17 for SQL SERVER'
engine = create_engine("mssql+pyodbc://@DESKTOP-1KEA5IJ/database?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes")
con = engine.connect()
df_expanded.to_sql('Vagas_linkedin', con=con, index=False, if_exists="replace")

