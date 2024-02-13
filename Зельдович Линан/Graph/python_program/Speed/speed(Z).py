import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.animation import FuncAnimation
from scipy.optimize import curve_fit


def func(x, k, b):
    return k * x + b

data = np.loadtxt("../../../Data/Speed/Z/Le_F = 1, Le_X = 1, R = 0.005, q = 0.9, sigma = 0.15.txt")
#data_old = np.loadtxt("../data/speed_old.txt")


speed = data[:, 0]
z = data[:, 1]

popt, pcov = curve_fit(func, np.log(z), np.log(speed))
print(popt)
k = popt[0]
b = popt[1]

#speed_old = data_old[:, 0]
#z_old = data_old[:, 1]


fig = plt.figure()

plt.plot(z, speed, '.', color = 'r')
plt.plot(z, z**k*np.exp(b), color = 'b')

#plt.plot(np.log(z), np.log(speed), '.', color = 'r')
#plt.plot(np.log(z), k*np.log(z)+b, color = 'r')


#plt.plot(z_old, speed_old, '.',color = 'g')




plt.legend(['Данные', str(np.exp(b).round(2))+'$\cdot z^{'+str(k.round(2))+'}$ - аппроксимация '], loc = 'best')

#plt.plot(x, w[frame,:], color = 'g')
plt.xlabel('z')
plt.ylabel('speed')


plt.grid()
 
    
