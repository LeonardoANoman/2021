import pandas as pd
import numpy as np

dfa = pd.DataFrame(np.arange(15).reshape(5,3))
dfb = pd.DataFrame((np.arange(9)**2).reshape(3,3))

print(pd.concat([dfa,dfb], ignore_index=True))

df1 = pd.DataFrame({"id": [1,2,3], "cor": ["branco","preto","verde"]})
df2 = pd.DataFrame({"times": ["time1","time2","time3","time4","time5"], "id": [1,1,2,3,2]})
print(pd.merge(df1,df2))