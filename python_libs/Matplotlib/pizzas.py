import matplotlib.pyplot as plt

nomes = ["A","B","C","D","E"]
valores = [10,20,30,30,10]
explodir = (0,0,0.1,0,0)

plt.pie(valores, labels=nomes, autopct="%1.1f%%", explode=explodir)

plt.show()