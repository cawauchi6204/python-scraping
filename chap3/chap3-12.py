import pandas as pd

df = pd.read_csv('chap3/test.csv')

kokugo = df.sort_values('国語',ascending=False)
kokugo.to_csv('export3.csv',index=False,header=False)
