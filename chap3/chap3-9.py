import pandas as pd

df = pd.read_csv('chap3/test.csv')

kokugo = df.sort_values('国語',ascending=False)
print('国語の点数が高いもの順でソート',kokugo)
