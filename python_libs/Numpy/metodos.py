import numpy as np

a = np.arange(8).reshape(2,4)**2
a[0][0] = 11

print(a.max())
print(a.max(axis=1))

print(a.argmax())
print(a.sum())
print(a.mean())
print(a.std())
print(a.cumsum())