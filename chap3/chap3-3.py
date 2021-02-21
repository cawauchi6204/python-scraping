import pandas as pd

df = pd.read_csv('chap3/test.csv')

print('国語の列データ\n',df['国語'])

print('国語と数学の列データ\n',df[['国語','数学']])
