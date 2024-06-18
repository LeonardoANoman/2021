import pandas as pd
import numpy as np

file = "Pandas\Players.csv"

df = pd.read_csv(file)

a_arr = np.arange(20).reshape(4,5)

df_columns = ["A","B","C","D","E"]

a_df = pd.DataFrame(a_arr,columns=df_columns)
print(a_df)
print(a_df.drop(index=2))
print(a_df.drop(columns="D"))

a_df.isnull() # retorna True ou False 
a_df.notnull() # retorna True ou False 

a_df.dropna() # remove valores NaN
a_df.fillna(value=50) # preenche valores NaN com 50

a_df.duplicated() # retorna True se a linha inteira for duplicada
a_df.drop_duplicates() # remove linha duplicada