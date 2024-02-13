import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.animation import FuncAnimation
from scipy.optimize import curve_fit


def func(x, k, b):
    return k * x + b

data = np.loadtxt("../../../Data/Speed/Le_F/Z = 8, Le_X = 1, R = 0.005, q = 0.9, sigma = 0.15.txt")


speed = data[:, 0]
Le_F = data[:, 1]

popt, pcov = curve_fit(func, np.log(Le_F), np.log(speed))

print(popt)
k = popt[0]
b = popt[1]

fig = plt.figure()

plt.plot(Le_F, speed, '.', color = 'r')
plt.plot(Le_F, Le_F**k*np.exp(b), color = 'b')

#plt.plot(np.log(Le_F), np.log(speed), '.', color = 'r')
#plt.plot(np.log(Le_F), k*np.log(Le_F) + b, color = 'b')





plt.legend(['Данные', str(np.exp(b).round(2))+'$\cdot Le_F^{'+str(k.round(2))+'}$ - аппроксимация '], loc = 'best')

#plt.plot(x, w[frame,:], color = 'g')
plt.xlabel('Le_F')
plt.ylabel('speed')


plt.grid()