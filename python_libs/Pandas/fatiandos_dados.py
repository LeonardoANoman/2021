import pandas as pd

file = "Pandas\Players.csv"

df = pd.read_csv(file)

print(df.loc[1:4,["height", "birth_state"]])

print(df.iloc[0:10:2,2:5])