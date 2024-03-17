import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt



x = np.linspace(0, 4, 12)
y = np.cos(x**2/3+4)

f2 = interpolate.interp1d(x, y, kind = 'cubic')

xnew = np.linspace(0, 4, 1000)

plt.plot(xnew, f2(xnew), '--')

plt.plot(x, y, '.')
plt.grid()
plt.show()