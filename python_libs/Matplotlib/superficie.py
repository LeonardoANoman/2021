import matplotlib.pyplot as plt
import numpy as np

a = np.arange(3)
malha = np.meshgrid(a,a)
z = np.array([[0,0,0], [0,0,0] ,[0,0,0]])

pi = np.linspace(0,np.pi,50)
malha_2 = np.meshgrid(pi,pi)
z_2 = np.sin(malha_2[0])*np.sin(malha_2[1])

fig = plt.figure()
ax = fig.gca(projection = "3d")
surf =ax.plot_surface(malha_2[0], malha_2[1], z)