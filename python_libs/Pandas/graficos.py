import pandas as pd
import numpy as np

arr = np.arange(10)

serie_1 = pd.Series(arr)
serie_1.plot() # gráfico

df.plot.bar() # gráfico de barras
df.plot.bar(y="quantidade") # gráfico de barras
df.plot.pie(y="quantidade") # gráfico de pizza
df.plot.scatter(x="altura", y="peso") # gráfico de dispersão