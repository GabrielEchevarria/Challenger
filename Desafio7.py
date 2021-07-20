# Agregar métricas a un DataFrame.

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


df7=df[[ 'itemId','availableQuantity']].copy()
df7['stockPercentage']=(df7['availableQuantity']/df7['availableQuantity'].sum())*100
df7['stockPercentage']=df7['stockPercentage'].round(2)
df7.sort_values('stockPercentage', ascending=False, inplace=True)

print(df7)