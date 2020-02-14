'''
Created on 3 feb. 2020

@author: jramosm
'''

import pandas as pd

 
df = pd.read_csv( 'C:\\Users\\jramosm\\Downloads\\timelog.csv', sep=';', encoding='utf-8' )
         
         
# gk = df.groupby('Fecha') 
         
# df.apply(lambda x: pd.lib.infer_dtype(x.values))

print(df) 
