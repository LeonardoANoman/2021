import numpy as np

a1 = np.ones(6)*11
print(a1)

a2 = np.arange(0,10,0.5)
print(a2)

a3 = np.linspace(0,10,12)
print(a3)

a4 = np.ones(8)
a4.reshape(2,4)

a5 = np.zeros(8)
a5.reshape(2,4)

a6 = np.vstack((a4, a5))
a7 = np.hstack((a4, a5))