import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_csv('chap4/FEH_00200524_190618234018.csv',index_col='全国・都道府県',encoding='shift_jis')

df = df.drop('全国',axis=0)

df['平成30年'] = pd.to_numeric(df['平成30年'].str.replace(',',''))
df['平成30年'].plot.bar()
plt.show()
