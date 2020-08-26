import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mplc
import matplotlib.cm as cm
from scipy.stats import gaussian_kde

def kdeplot(x,y,xnorm,ynorm):
    xy = np.vstack([x,y])
    z = gaussian_kde(xy)(xy)

    wt = 1.0*len(x)/(len(xnorm)*1.0)
    norm = mplc.Normalize(vmin=0, vmax=8/wt)
    cmap = cm.gnuplot

    idx = z.argsort()
    x, y, z = x[idx], y[idx], z[idx]

    args = (x,y)
    kwargs = {'c':z,'s':10,'edgecolor':'','cmap':cmap,'norm':norm}

    return args, kwargs

#x1 = np.random.normal(size=1000)
#
#xy = np.vstack([x,y])
#z = gaussian_kde(xy)(xy)

#idx = z.argsort()

#fig,ax = plt.subplots()
#ax.scatter(x,y,c=z,s=50,edgecolor='')
#plt.show()

# (x1,y1) is some data set whose density map coloring you 
# want to scale to (xnorm,ynorm)
args,kwargs = kdeplot(x1,y1,xnorm,ynorm)
plt.scatter(*args,**kwargs)