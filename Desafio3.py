"""
Deserializar un JSON
"""

import pandas as pd
import numpy as np
from datetime import datetime
import os

file_json='C:/Users/gechevarria/Documents/Sellers.json'
file_name='sellers_x_segmento.csv'
hoy = datetime.today()

df_json= pd.read_json(file_json)
df=pd.json_normalize(df_json.body)

df=df[['site_id','id','nickname','points']]
df.columns=['siteId','sellerId','sellerNickname','sellerPoints']

df['segmento']=np.where(df['sellerPoints']<0,'Negativo',np.where(df['sellerPoints']>0,'Positivo','Cero'))

# Tomo los sitios únicos
sites=df['siteId'].unique()

# Tomo los segmentos únicos para separar en carpetas
segments=df['segmento'].unique()

for site in sites:
    df_temp=df[df['siteId']==site]
    for segmento in segments:
        path = site+hoy.strftime('/%Y/%m/%d/')+segmento
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
        df_out=df_temp[df['segmento']==segmento]
        df_out.to_csv(os.path.join(path,file_name),index=False)
