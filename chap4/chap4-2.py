import pandas as pd

df = pd.read_csv('chap4/13TOKYO.CSV',header=None,encoding='shift_jis')

results = df[df[2] == 1240003]
print(results[[2,6,7,8]])
