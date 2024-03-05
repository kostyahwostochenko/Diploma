import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.animation import FuncAnimation
from scipy.optimize import curve_fit



def func(x, k, b):
    return k*x**b

data_1 = np.loadtxt("../../Data/Temperature/Le_F = 1, Le_X = 1, R = 0.005, q = 0.9, sigma = 0.15.txt")
data_2 = np.loadtxt("../../Data/Temperature/Le_F = 1.5, Le_X = 1, R = 0.005, q = 0.9, sigma = 0.15.txt")
#data_3 = np.loadtxt("../../../Data/Speed/R/Z = 8, Le_F = 1.5, Le_X = 1, q = 0.9, sigma = 0.15.txt")


speed_1 = data_1[:, 0]
Z_1 = data_1[:, 1]

speed_2 = data_2[:, 0]
Z_2 = data_2[:, 1]

#speed_3 = data_3[:, 0]
#Z_3 = data_3[:, 1]

'''
popt, pcov = curve_fit(func, R, speed)

print(popt)
k = popt[0]
b = popt[1]
'''

fig = plt.figure()

plt.grid(True)

plt.plot(Z_1, speed_1, '-', color = 'r')
plt.plot(Z_1, 1 - 1/Z_1, '-')
#plt.plot(Z_2, speed_2, '-', color = 'b')
#plt.plot(Z_3, speed_3, '-', color = 'g')
#plt.text(0, 0.5, "HELLO!", fontsize=15)
#plt.plot(R, k*R**b, color = 'b')


#plt.plot(np.log(R), np.log(speed), '.', color = 'r')
#plt.plot(np.log(R), k*np.log(R) + b, color = 'b')

