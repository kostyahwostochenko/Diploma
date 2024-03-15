import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.animation import FuncAnimation
from scipy.optimize import curve_fit
from scipy.optimize import fsolve




data_theta_1 = np.loadtxt("../../Data/Temperature/Le_F = 1, Le_X = 1, R = 1, q = 0.9, sigma = 0.15.txt")
data_theta_2 = np.loadtxt("../../Data/Temperature/Le_F = 1, Le_X = 1, R = 0.1, q = 0.9, sigma = 0.15.txt")
data_theta_3 = np.loadtxt("../../Data/Temperature/Le_F = 1, Le_X = 1, R = 0.005, q = 0.9, sigma = 0.15.txt")

data_height_1 = np.loadtxt("../../Data/Height/Z/Le_F = 1, Le_X = 1, R = 1, q = 0.9, sigma = 0.15.txt")
data_height_2 = np.loadtxt("../../Data/Height/Z/Le_F = 1, Le_X = 1, R = 0.1, q = 0.9, sigma = 0.15.txt")
data_height_3 = np.loadtxt("../../Data/Height/Z/Le_F = 1, Le_X = 1, R = 0.005, q = 0.9, sigma = 0.15.txt")

data_speed_1 = np.loadtxt("../../Data/Speed/Z/Le_F = 1, Le_X = 1, R = 1, q = 0.9, sigma = 0.15.txt")
data_speed_2 = np.loadtxt("../../Data/Speed/Z/Le_F = 1, Le_X = 1, R = 0.1, q = 0.9, sigma = 0.15.txt")
data_speed_3 = np.loadtxt("../../Data/Speed/Z/Le_F = 1, Le_X = 1, R = 0.005, q = 0.9, sigma = 0.15.txt")


X_0_1 = data_height_1[:, 0]
speed_1 = data_speed_1[:, 0]
theta_1 = data_theta_1[:, 0]
Z_1 = data_theta_1[:, 2]

X_0_2 = data_height_2[:, 0]
speed_2 = data_speed_2[:, 0]
theta_2 = data_theta_2[:, 0]
Z_2 = data_theta_2[:, 1]

X_0_3 = data_height_3[:, 0]
speed_3 = data_speed_3[:, 0]
theta_3 = data_theta_3[:, 0]
Z_3 = data_theta_3[:, 1]



R_1 = 1
R_2 = 0.1
R_3 = 0.005

q = 0.9
sigma = 0.15
Le_X = 1
Le_F = 1


dot_cnt = 100
Z_an = np.linspace(5, 15, dot_cnt)

X_0_1_an = np.linspace(5, 15, dot_cnt)
X_0_2_an = np.linspace(5, 15, dot_cnt)
X_0_3_an = np.linspace(5, 15, dot_cnt)

speed_1_an = np.linspace(5, 15, dot_cnt)
speed_2_an = np.linspace(5, 15, dot_cnt)
speed_3_an = np.linspace(5, 15, dot_cnt)


def amp(R):
    return Le_X*Le_F/(2*R*(1-sigma)**2)

def func_1(x):
    return 2*x + Le_X*(1 - x)

def func_2(x):
    return q*(1 - sigma)*x*(1 + x)

def func(x, z, R):
    return amp(R)*np.exp(z*func_2(x)/(func_2(x) - func_1(x))) - x/(1-x)**2


for i in range(0, len(Z_an), 1):
    
    X_0_1_an[i] = fsolve(func, 0.5, (Z_an[i], R_1))
    
    X_0_2_an[i] = fsolve(func, 0.5, (Z_an[i], R_2))
    
    X_0_3_an[i] = fsolve(func, 0.5, (Z_an[i], R_3))
    
    
    
theta_1_an = 1 - q*(1-sigma)*X_0_1_an*(1 + X_0_1_an)/(2*X_0_1_an + Le_X*(1-X_0_1_an))
theta_2_an = 1 - q*(1-sigma)*X_0_2_an*(1 + X_0_2_an)/(2*X_0_2_an + Le_X*(1-X_0_2_an))
theta_3_an = 1 - q*(1-sigma)*X_0_3_an*(1 + X_0_3_an)/(2*X_0_3_an + Le_X*(1-X_0_3_an))

speed_1_an = np.sqrt(4*R_1*X_0_1_an**2/(Le_X*(1 - X_0_1_an**2)))
speed_2_an = np.sqrt(4*R_2*X_0_2_an**2/(Le_X*(1 - X_0_2_an**2)))
speed_3_an = np.sqrt(4*R_3*X_0_3_an**2/(Le_X*(1 - X_0_3_an**2)))



fig, ax = plt.subplots(nrows = 1, ncols = 3, figsize=(16, 4))


ax[0].set_xlabel(r'$\beta$')
ax[0].set_ylabel(r'$\theta_0$')

ax[1].set_xlabel(r'$\beta$')
ax[1].set_ylabel(r'$X_0$')

ax[2].set_xlabel(r'$\beta$')
ax[2].set_ylabel(r'$c$')



ax[0].plot(Z_1, theta_1, '-', color = 'r')
ax[0].plot(Z_2, theta_2, '-', color = 'b')
ax[0].plot(Z_3, theta_3, '-', color = 'g')

ax[0].plot(Z_an, theta_1_an, '--', color = 'r')
ax[0].plot(Z_an, theta_2_an, '--', color = 'b')
ax[0].plot(Z_an, theta_3_an, '--', color = 'g')



ax[1].plot(Z_1, X_0_1, '-', color = 'r')
ax[1].plot(Z_2, X_0_2, '-', color = 'b')
ax[1].plot(Z_3, X_0_3, '-', color = 'g')

ax[1].plot(Z_an, X_0_1_an, '--', color = 'r')
ax[1].plot(Z_an, X_0_2_an, '--', color = 'b')
ax[1].plot(Z_an, X_0_3_an, '--', color = 'g')



ax[2].plot(Z_1, speed_1, '-', color = 'r')
ax[2].plot(Z_2, speed_2, '-', color = 'b')
ax[2].plot(Z_3, speed_3, '-', color = 'g')

ax[2].plot(Z_an, speed_1_an, '--', color = 'r')
ax[2].plot(Z_an, speed_2_an, '--', color = 'b')
ax[2].plot(Z_an, speed_3_an, '--', color = 'g')

            



ax[0].legend(['$R = 1$', '$R = 0.1$', '$R = 0.005$'])
ax[1].legend(['$R = 1$', '$R = 0.1$', '$R = 0.005$'])
ax[2].legend(['$R = 1$', '$R = 0.1$', '$R = 0.005$'])

ax[0].grid(True)
ax[1].grid(True)
ax[2].grid(True)


plt.tight_layout()
plt.show()
