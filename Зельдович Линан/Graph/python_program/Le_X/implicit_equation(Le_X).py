import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.animation import FuncAnimation
from scipy.optimize import curve_fit
from scipy.optimize import fsolve




data_height_1 = np.loadtxt("../../../Data/Height/Le_X/Z = 8, Le_F = 1, R = 0.005, q = 0.9, sigma = 0.15.txt")

data_speed_1 = np.loadtxt("../../../Data/Speed/Le_X/Z = 8, Le_F = 1, R = 0.005, q = 0.9, sigma = 0.15.txt")



X_0_1 = data_height_1[:, 0]
speed_1 = data_speed_1[:, 0]
Le_X_1 = data_height_1[:, 2]




z = 8
R = 0.005
q = 0.9
sigma = 0.15
Le_F = 1



dot_cnt = 100
Le_X_an = np.linspace(0.5, 2, dot_cnt)

X_0_1_an = np.linspace(0.5, 2, dot_cnt)

speed_1_an = np.linspace(0.5, 2, dot_cnt)



def amp(Le_X):
    return Le_X*Le_F/(2*R*(1-sigma)**2)

def func_1(x, Le_X):
    return 2*x + Le_X*(1 - x)

def func_2(x):
    return q*(1 - sigma)*x*(1 + x)

def func(x, Le_X):
    return amp(Le_X)*np.exp(z*func_2(x)/(func_2(x) - func_1(x, Le_X))) - x/(1-x)**2


for i in range(0, len(Le_X_an), 1):
    
    X_0_1_an[i] = fsolve(func, 0.5, Le_X_an[i])
    
    

speed_1_an = np.sqrt(4*R*X_0_1_an**2/(Le_X_an*(1 - X_0_1_an**2)))




fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize=(12, 5))



ax[0].set_xlabel(r'$L_X$')
ax[0].set_ylabel(r'$X_0$')

ax[1].set_xlabel(r'$L_X$')
ax[1].set_ylabel(r'$c$')


ax[0].plot(Le_X_1, X_0_1, '-', color = 'r')
ax[0].plot(Le_X_an, X_0_1_an, '--', color = 'r')


ax[1].plot(Le_X_1, speed_1, '-', color = 'r')
ax[1].plot(Le_X_an, speed_1_an, '--', color = 'r')





ax[0].grid(True)
ax[1].grid(True)



plt.tight_layout()
plt.show()