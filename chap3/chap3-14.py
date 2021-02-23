import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_csv('chap3/test.csv')

df.plot()
plt.show()
