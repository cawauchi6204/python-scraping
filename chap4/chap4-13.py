import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df1 = pd.read_csv('chap4/sample_1.csv',index_col='時点')

df1['年平均気温【℃】'].plot()
plt.ylim(-10,40)
plt.show()
