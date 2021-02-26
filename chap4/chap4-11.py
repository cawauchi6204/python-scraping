import pandas as pd

df1 = pd.read_csv("chap4/sample_1.csv",index_col="時点")
df2 = pd.read_csv("chap4/sample_2.csv",index_col="時点")
df3 = pd.read_csv("chap4/sample_3.csv",index_col="時点")

print(df1.columns.values)
print(df2.columns.values)
print(df3.columns.values)
