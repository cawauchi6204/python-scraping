import pandas as pd

df = pd.read_csv('chap3/test.csv')

print('行と列を入れ替える\n',df.T)

print('Pythonのリストデータ化\n',df.values)
