import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.optimize import curve_fit



data = np.loadtxt("../../../Data/Height/Le_F/Z = 8, Le_X = 1, R = 0.005, q = 0.9, sigma = 0.15.txt")


height = data[:, 0]
width = data[:, 1]
Le_F = data[:, 2]



def func(x, k, b):
    return k*x**b

'''
popt, pcov = curve_fit(func, z, height)

print(popt)
k = popt[0]
b = popt[1]
'''

fig = plt.figure()

plt.plot(Le_F, height, '-', color = 'r')

#plt.plot(z, k*z**b, '-', color = 'b')




#plt.legend(['q = 0.2', 'q = 0.5', 'q = 0.9'])
plt.xlabel('Le_F')
plt.ylabel('Height')
plt.title('Dependence of height on Le_F')


plt.grid()