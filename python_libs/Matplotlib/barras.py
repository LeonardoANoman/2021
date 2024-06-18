import matplotlib.pyplot as plt
import numpy as np

nomes = ["A","B","C","D"]
valores = [20,50,10,30]
valores2 = [10,20,30,20]

plt.bar(nomes,valores,color="k")
plt.bar(nomes,valores2,color="r")

plt.show()

fig, ax = plt.subplots()

x = np.arange(4)

largura = 0.4

rect1 = ax.bar(x+largura/2, valores, color="k", width=largura, label="grafico 1")
rect2 = ax.bar(x-largura/2, valores2, color="r", width=largura, label="grafico 2")

ax.set_xticks(x)
ax.set_xtickslabels(nomes)
plt.legend()

plt.show()