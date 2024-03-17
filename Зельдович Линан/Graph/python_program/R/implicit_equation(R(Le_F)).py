import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt



data_1_speed = np.loadtxt("../../../Data/Speed/R/Z = 8, Le_F = 0.5, Le_X = 1, q = 0.9, sigma = 0.15.txt")
data_2_speed = np.loadtxt("../../../Data/Speed/R/Z = 8, Le_F = 1, Le_X = 1, q = 0.9, sigma = 0.15.txt")
data_3_speed = np.loadtxt("../../../Data/Speed/R/Z = 8, Le_F = 1.5, Le_X = 1, q = 0.9, sigma = 0.15.txt")

data_1_height = np.loadtxt("../../../Data/Height/R/Z = 8, Le_F = 0.5, Le_X = 1, q = 0.9, sigma = 0.15.txt")
data_2_height = np.loadtxt("../../../Data/Height/R/Z = 8, Le_F = 1, Le_X = 1, q = 0.9, sigma = 0.15.txt")
data_3_height = np.loadtxt("../../../Data/Height/R/Z = 8, Le_F = 1.5, Le_X = 1, q = 0.9, sigma = 0.15.txt")


speed_1 = data_1_speed[:, 0]
R_1 = data_1_speed[:, 1]
X_0_1 = data_1_height[:, 0]

speed_2 = data_2_speed[:, 0]
R_2 = data_2_speed[:, 1]
X_0_2 = data_2_height[:, 0]

speed_3 = data_3_speed[:, 0]
R_3 = data_3_speed[:, 1]
X_0_3 = data_3_height[:, 0]

z = 8
q = 0.9
sigma = 0.15
Le_X = 1

Le_F_1 = 0.5
Le_F_2 = 1
Le_F_3 = 1.5 

dot_cnt = 100
R_an = np.linspace(0.005, 0.5, dot_cnt)
X_0_1_an = np.linspace(0.005, 0.5, dot_cnt)
X_0_2_an = np.linspace(0.005, 0.5, dot_cnt)
X_0_3_an = np.linspace(0.005, 0.5, dot_cnt)

def amp(R, Le_F):
    return Le_X*Le_F/(2*R*(1-sigma)**2)

def func_1(x):
    return 2*x + Le_X*(1 - x)

def func_2(x):
    return q*(1 - sigma)*x*(1 + x)

def func(x, R, Le_F):
    return amp(R, Le_F)*np.exp(z*func_2(x)/(func_2(x) - func_1(x))) - x/(1-x)**2



# Сначала передается функция, в которую подставляется x, затем его начальное
# приближение, а потом дополнительные аргументы функции func

for i in range(0, len(R_an), 1):
    
    X_0_1_an[i] = fsolve(func, 0.5, (R_an[i], Le_F_1))
    
    X_0_2_an[i] = fsolve(func, 0.5, (R_an[i], Le_F_2))

    X_0_3_an[i] = fsolve(func, 0.5, (R_an[i], Le_F_3))
    
    
speed_1_an = np.sqrt(4*R_an*X_0_1_an**2/(Le_X*(1 - X_0_1_an**2)))
speed_2_an = np.sqrt(4*R_an*X_0_2_an**2/(Le_X*(1 - X_0_2_an**2)))
speed_3_an = np.sqrt(4*R_an*X_0_3_an**2/(Le_X*(1 - X_0_3_an**2)))



fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize=(12, 5))



ax[0].set_xlabel(r'$R$')
ax[0].set_ylabel(r'$X_0$')

ax[1].set_xlabel(r'$R$')
ax[1].set_ylabel(r'$c$')



ax[0].plot(R_1, X_0_1, '-', color = 'r')
ax[0].plot(R_2, X_0_2, '-', color = 'b')
ax[0].plot(R_3, X_0_3, '-', color = 'g')

ax[0].plot(R_an, X_0_1_an, '--', color = 'r')
ax[0].plot(R_an, X_0_2_an, '--', color = 'b')
ax[0].plot(R_an, X_0_3_an, '--', color = 'g')



ax[1].plot(R_1, speed_1, '-', color = 'r')
ax[1].plot(R_2, speed_2, '-', color = 'b')
ax[1].plot(R_3, speed_3, '-', color = 'g')

ax[1].plot(R_an, speed_1_an, '--', color = 'r')
ax[1].plot(R_an, speed_2_an, '--', color = 'b')
ax[1].plot(R_an, speed_3_an, '--', color = 'g')
            


ax[0].legend(['$Le_F = 0.5$', '$Le_F = 1$', '$Le_F = 1.5$'])
ax[1].legend(['$Le_F = 0.5$', '$Le_F = 1$', '$Le_F = 1.5$'])

ax[0].grid(True)
ax[1].grid(True)


plt.tight_layout()
plt.show()
