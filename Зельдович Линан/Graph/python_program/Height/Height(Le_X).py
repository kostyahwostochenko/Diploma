import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.optimize import curve_fit



data = np.loadtxt("../../../Data/Height/Le_X/Z = 8, Le_F = 1, R = 0.005, q = 0.9, sigma = 0.15.txt")


height = data[:, 0]
width = data[:, 1]
Le_X = data[:, 2]



def func(x, k, b):
    return k*x**b

'''
popt, pcov = curve_fit(func, z, height)

print(popt)
k = popt[0]
b = popt[1]
'''

fig = plt.figure()

plt.plot(Le_X, height, '-', color = 'r')

#plt.plot(z, k*z**b, '-', color = 'b')




#plt.legend(['q = 0.2', 'q = 0.5', 'q = 0.9'])
plt.xlabel(r'$Le_x$')
plt.ylabel('Height, $X_0$')
plt.title('Dependence of height $X_0$ on $Le_x$')


plt.grid()