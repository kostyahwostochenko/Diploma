import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.optimize import curve_fit



data_1 = np.loadtxt("../../../Data/Height/R/Z = 8, Le_F = 1, Le_X = 1, q = 0.2, sigma = 0.15.txt")
data_2 = np.loadtxt("../../../Data/Height/R/Z = 8, Le_F = 1, Le_X = 1, q = 0.5, sigma = 0.15.txt")
data_3 = np.loadtxt("../../../Data/Height/R/Z = 8, Le_F = 1, Le_X = 1, q = 0.9, sigma = 0.15.txt")

height_1 = data_1[:, 0]
width_1 = data_1[:, 1]
R_1 = data_1[:, 2]

height_2 = data_2[:, 0]
width_2 = data_2[:, 1]
R_2 = data_2[:, 2]

height_3 = data_3[:, 0]
width_3 = data_3[:, 1]
R_3 = data_3[:, 2]


def func(x, k, b):
    return k*x**b

'''
popt, pcov = curve_fit(func, z, height)

print(popt)
k = popt[0]
b = popt[1]
'''

fig = plt.figure()

plt.plot(R_1, height_1, '-', color = 'r')
plt.plot(R_2, height_2, '-', color = 'b')
plt.plot(R_3, height_3, '-', color = 'g')
#plt.plot(z, k*z**b, '-', color = 'b')




plt.legend(['q = 0.2', 'q = 0.5', 'q = 0.9'])
plt.xlabel('R')
plt.ylabel('Height')
plt.title('Dependence of height on R')


plt.grid()