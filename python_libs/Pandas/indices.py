import pandas as pd

file = "Pandas\Players.csv"

df = pd.read_csv(file)

from_california = df["birth_state"] == 'California'

print(df[from_california].head())

after_1970 = df['born']>1970
print(df[after_1970])