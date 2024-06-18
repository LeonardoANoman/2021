import matplotlib.pyplot as plt
import numpy as np

xa_array = np.linspace(0,2*np.pi,500)
ya_array = np.sin(xa_array)

xb_array = np.linspace(0,2*np.pi,500)
yb_array = np.sin(xb_array + np.pi/2)

plt.plot(xa_array, ya_array) # gráfico
plt.plot(xb_array, yb_array) # gráfico
plt.xlabel("x") # nome do eixo x
plt.ylabel("y") # nome do eixo y
plt.grid()

fig, ax = plt.subplots()

ax.plot(xa_array, ya_array, "k-", label="func a")
ax.plot(xb_array, yb_array, "r-", label="func b")
ax.set_title("Função")
plt.legend()