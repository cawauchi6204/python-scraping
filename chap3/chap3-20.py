import pandas as pd
import openpyxl

df = pd.read_csv('chap3/test.csv')

kokugo = df.sort_values('国語',ascending=False)

kokugo.to_exel('csv_to_excel1.xlsx',index=False,sheet_name='国語でソート')
