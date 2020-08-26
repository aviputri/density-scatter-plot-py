#color-coded
import numpy as np
import mpl_scatter_density
import matplotlib.pyplot as plt

N = 10000000
x = np.random.normal(4, 2, N)
y = np.random.normal(3, 1, N)
c = x - y + np.random.normal(0, 5, N)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='scatter_density')
ax.scatter_density(x, y, c=c, vmin=-10, vmax=+10, cmap=plt.cm.RdYlBu)
ax.set_xlim(-5, 13)
ax.set_ylim(-5, 11)
#fig.savefig('gaussian_color_coded.png')
plt.show()