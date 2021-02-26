import pandas as pd

df = pd.read_csv('chap4/13TOKYO.CSV',header=None,encoding='shift_jis')

results = df[df[8] == '四谷']
print(results[[2,6,7,8]])

results = df[df[8].str.contains('四谷')]
print(results[[2,6,7,8]])
