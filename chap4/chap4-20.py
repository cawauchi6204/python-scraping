import pandas as pd

df = pd.read_csv('chap4/898.csv')

store = df[['緯度', '経度']].values
print(len(store))
print(store)
