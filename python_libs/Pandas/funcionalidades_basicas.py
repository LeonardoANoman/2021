import pandas as pd

lista_a = ["a", "a", "b" ,"c", "a", "d", "c"]
lista_b = list(range(7))
dict1 = {"string": lista_a, "numeros": lista_b}
df = pd.DataFrame(dict1)
print(df)
print(df.head())
print(df.tail())
print(df['string'].value_counts())
print(df.sort_values(by="string"))
print(df.sum())
print(df["numeros"].mean())
print(df["numeros"].median())