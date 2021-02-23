import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_csv('chap3/test.csv',index_col=0)


colorlist = ['skyblue','steelblue','tomato','cadetblue','orange','sienna']

df.T.plot.bar(color=colorlist)
plt.legend(loc="lower right")
plt.show()
