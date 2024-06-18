import pandas as pd
import numpy as np

lista_a = [11,22,33,44,55]
lista_b = ["a","b","c","d","e"]

serie_a = pd.Series(lista_a)
print(serie_a)

serie_a = pd.Series(lista_a, index=lista_b)
print(serie_a)
print(serie_a["b"])

arr = np.arange(10)**2
serie_c = pd.Series(arr)
print(serie_c)

dict1 ={"coluna1": np.arange(10)*5, "coluna2": np.arange(10)**2, "coluna3": np.ones(10)}
df1 = pd.DataFrame(dict1)
print(df1)

# pd.read_csv(file)

