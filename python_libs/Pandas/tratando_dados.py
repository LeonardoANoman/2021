import pandas as pd

file = "Pandas\Players.csv"

df = pd.read_csv(file)

print(df.head())
print(df.columns)
print(df["height"].mean())
print(df["weight"].mean())

razao = df["weight"]/df["height"]
df["razao"] = razao

print(df.min())
print(df.max())

print(df["birth_state"].value_counts())
print(df.sort_values(by="height").tail())