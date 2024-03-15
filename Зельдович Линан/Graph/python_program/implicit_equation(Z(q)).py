import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

data_1_speed = np.loadtxt("../../Data/Speed/Z/Le_F = 1, Le_X = 1, R = 0.005, q = 0.9, sigma = 0.15.txt")
data_2_speed = np.loadtxt("../../Data/Speed/Z/Le_F = 1, Le_X = 1, R = 0.005, q = 0.5, sigma = 0.15.txt")

data_1_height = np.loadtxt("../../Data/Height/Z/Le_F = 1, Le_X = 1, R = 0.005, q = 0.9, sigma = 0.15.txt")
data_2_height = np.loadtxt("../../Data/Height/Z/Le_F = 1, Le_X = 1, R = 0.005, q = 0.5, sigma = 0.15.txt")



speed_1 = data_1_speed[:, 0]
Z_1 = data_1_speed[:, 1]
X_0_1 = data_1_height[:, 0]

speed_2 = data_2_speed[:, 0]
Z_2 = data_2_speed[:, 1]
X_0_2 = data_2_height[:, 0]


R = 0.005
sigma = 0.15
Le_F = 1
Le_X = 1

q_1 = 0.9
q_2 = 0.5

dot_cnt = 100
Z_an = np.linspace(5, 15, dot_cnt)
X_0_1_an = np.linspace(5, 15, dot_cnt)
X_0_2_an = np.linspace(5, 15, dot_cnt)


def amp():
    return Le_X*Le_F/(2*R*(1-sigma)**2)

def func_1(x):
    return 2*x + Le_X*(1 - x)

def func_2(x, q):
    return q*(1 - sigma)*x*(1 + x)

def func(x, z, q):
    return amp()*np.exp(z*func_2(x, q)/(func_2(x, q) - func_1(x))) - x/(1-x)**2



# Сначала передается функция, в которую подставляется x, затем его начальное
# приближение, а потом дополнительные аргументы функции func

for i in range(0, len(Z_an), 1):

    X_0_1_an[i] = fsolve(func, 0.5, (Z_an[i], q_1))
    
    X_0_2_an[i] = fsolve(func, 0.5, (Z_an[i], q_2))

    
speed_1_an = np.sqrt(4*R*X_0_1_an**2/(Le_X*(1 - X_0_1_an**2)))
speed_2_an = np.sqrt(4*R*X_0_2_an**2/(Le_X*(1 - X_0_2_an**2)))




fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize=(12, 5))

ax[0].set_xlabel(r'$\beta$')
ax[0].set_ylabel(r'$X_0$')

ax[1].set_xlabel(r'$\beta$')
ax[1].set_ylabel(r'$c$')



ax[0].plot(Z_1, X_0_1, '-', color = 'r')
ax[0].plot(Z_2, X_0_2, '-', color = 'b')


ax[0].plot(Z_an, X_0_1_an, '--', color = 'r')
ax[0].plot(Z_an, X_0_2_an, '--', color = 'b')



ax[1].plot(Z_1, speed_1, '-', color = 'r')
ax[1].plot(Z_2, speed_2, '-', color = 'b')


ax[1].plot(Z_an, speed_1_an, '--', color = 'r')
ax[1].plot(Z_an, speed_2_an, '--', color = 'b')
       



ax[0].legend([r'$q = 0.9$', r'$q = 0.5$'])
ax[1].legend([r'$q = 0.9$', r'$q = 0.5$'])

ax[0].grid(True)
ax[1].grid(True)


plt.tight_layout()
plt.show()