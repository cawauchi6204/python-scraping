import pandas as pd

df = pd.read_csv('chap4/FEH_00200524_190618234018.csv',index_col='全国・都道府県',encoding='shift_jis')
print(len(df))
print(df.columns.values)
