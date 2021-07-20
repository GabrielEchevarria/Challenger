# Parseo de un Array de Structs en un dataframe

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
print(df)
