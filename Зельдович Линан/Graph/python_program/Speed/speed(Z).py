import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.animation import FuncAnimation
from scipy.optimize import curve_fit



def func(x, k, b):
    return k*b**x


data_1 = np.loadtxt("../../../Data/Speed/Z/Le_F = 0.5, Le_X = 1, R = 0.005, q = 0.9, sigma = 0.15.txt")
data_2 = np.loadtxt("../../../Data/Speed/Z/Le_F = 1, Le_X = 1, R = 0.005, q = 0.9, sigma = 0.15.txt")
data_3 = np.loadtxt("../../../Data/Speed/Z/Le_F = 1.5, Le_X = 1, R = 0.005, q = 0.9, sigma = 0.15.txt")


speed_1 = data_1[:, 0]
Z_1 = data_1[:, 1]

speed_2 = data_2[:, 0]
Z_2 = data_2[:, 1]

speed_3 = data_3[:, 0]
Z_3 = data_3[:, 1]


popt_1, pcov_1 = curve_fit(func, Z_1, speed_1)
popt_2, pcov_2 = curve_fit(func, Z_2, speed_2)
popt_3, pcov_3 = curve_fit(func, Z_3, speed_3)

print(popt_1)
print(popt_2)
print(popt_3)

k_1 = popt_1[0]
b_1 = popt_1[1]

k_2 = popt_2[0]
b_2 = popt_2[1]

k_3 = popt_3[0]
b_3 = popt_3[1]

approx_1 = str(k_1.round(2)) + r'$\cdot \beta^{' + str(b_1.round(2)) + '}$'
approx_2 = str(k_2.round(2)) + r'$\cdot \beta^{' + str(b_2.round(2)) + '}$'
approx_3 = str(k_3.round(2)) + r'$\cdot \beta^{' + str(b_3.round(2)) + '}$'

'''
plt.plot(Z_1, k_1*Z_1**b_1, '-', color = 'r')
plt.plot(Z_2, k_2*Z_2**b_2, '-', color = 'b')
plt.plot(Z_3, k_3*Z_3**b_3, '-', color = 'g')
'''
plt.plot(Z_1, k_1*b_1**Z_1, '-', color = 'r')
plt.plot(Z_2, k_2*b_2**Z_2, '-', color = 'b')
plt.plot(Z_3, k_3*b_3**Z_3, '-', color = 'g')




plt.plot(Z_1, speed_1, '.', color = 'r')
plt.plot(Z_2, speed_2, '.', color = 'b')
plt.plot(Z_3, speed_3, '.', color = 'g')



plt.legend(['$Le_F$ = 0.5, ' + approx_1, '$Le_F$ = 1, ' + approx_2, '$Le_F$ = 1.5, ' + approx_3])
#plt.legend(['$q$ = 0.9', '$q$ = 0.5', '$Le_F$ = 1.5'])
plt.xlabel(r'$\beta$')
plt.ylabel('Speed')


plt.grid()
plt.show()





#plt.text(0, 0.5, "HELLO!", fontsize=15)
#plt.plot(R, k*R**b, color = 'b')
#plt.plot(np.log(R), np.log(speed), '.', color = 'r')
#plt.plot(np.log(R), k*np.log(R) + b, color = 'b')
#plt.legend(['Данные', str(np.exp(b).round(2))+'$\cdot R^{'+str(k.round(2))+'}$ - аппроксимация '], loc = 'best')
