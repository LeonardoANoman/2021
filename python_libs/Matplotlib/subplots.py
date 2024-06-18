import matplotlib.pyplot as plt
import numpy as np

xa_array = np.linspace(0,2,500)
ya_array = np.exp(xa_array)

fig, (ax1,ax2) = plt.subplots(2,2)
ax1[0].plot(xa_array, ya_array)
ax2[0].plot(xa_array, ya_array)