# Agregar las visitas al DataFrame con datos de ventas.

import pandas as pd
import json

file_json='MPE1004.json'

fj=open(file_json)
js=json.load(fj)

df=pd.DataFrame(js['results'])
df=df[[ 'id','sold_quantity','available_quantity']]
df.columns=['itemId','soldQuantity','availableQuantity']
df['rowId']=df.index+1
df=df[['rowId','itemId','soldQuantity','availableQuantity']]

#creo el DataFrame de las ventas
df5=df[['itemId','soldQuantity']]
#Cargo las visitas
file_csv='C:/Users/gechevarria/Documents/visits.csv'
df_visits=pd.read_csv(file_csv)

#Uno ambos DataFrame por itemId
df_result = df5.merge(df_visits, on='itemId', how='inner')
#filtro los items sin ventas
df_result = df_result[df_result['soldQuantity'] > 0]

print(df_result)