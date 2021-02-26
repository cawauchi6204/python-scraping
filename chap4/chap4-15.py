import pandas as pd

df = pd.read_csv("chap4/200.csv",encoding="shift-jis")

print(len(df))
print(df.columns.values)
