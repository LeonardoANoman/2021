import numpy as np
import matplotlib.pyplot as plt

x_array = np.linspace(0,10,500)
y_array = np.exp(x_array)

plt.figure()
plt.suptitle("Comparação escalas")
plt.subplot(211)
plt.plot(x_array, y_array, "r-")
plt.yscale("log")
plt.ylabel("Y log")
plt.grid()

plt.subplot(212)
plt.subplot(x_array, "k-")
plt.ylabel("Y linear")
plt.grid()