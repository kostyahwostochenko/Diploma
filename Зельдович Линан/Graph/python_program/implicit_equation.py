import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

data = np.loadtxt("../../Data/Speed/R/Z = 8, Le_F = 1, Le_X = 1, q = 0.9, sigma = 0.15.txt")


speed_1 = data[:, 0]
R_1 = data[:, 1]

z = 8
q = 0.9
sigma = 0.15
Le_X = 1
Le_F = 1

dot_cnt = 100
R = np.linspace(0.005, 0.5, dot_cnt)
Speed = np.linspace(0.005, 0.5, dot_cnt)
X_0 = np.linspace(0.005, 0.5, dot_cnt)

def amp(R):
    return Le_X*Le_F/(2*R*(1-sigma)**2)

def func_1(x):
    return 2*x + Le_X*(1 - x)

def func_2(x):
    return q*(1 - sigma)*x*(1 + x)

def func(x, R):
    return amp(R)*np.exp(z*func_2(x)/(func_2(x) - func_1(x))) - x/(1-x)**2



def func_11(x):
    return -2*x + Le_X*(1 + x)

def func_21(x):
    return q*(1 - sigma)*x*(1 - x)

def func1(x, R):
    return amp(R)*np.exp(z*func_21(x)/(func_21(x) - func_11(x))) - x/(1-x)**2

Speed1 = np.linspace(0.005, 0.5, dot_cnt)
X_01 = np.linspace(0.005, 0.5, dot_cnt)


# Сначала передается функция, в которую подставляется x, затем его начальное
# приближение, а потом дополнительные аргументы функции func

for i in range(0, len(R), 1):

    X_0[i] = fsolve(func, 0.5, R[i])
    X_01[i] = fsolve(func1, 0.5, R[i])
    
Speed = np.sqrt(4*R*X_0**2/(Le_X*(1 - X_0**2)))
Speed1 = np.sqrt(4*R*X_01**2/(Le_X*(1 - X_01**2)))
    
#plt.plot(R_1, speed_1, '-', color = 'r')
plt.plot(R, X_0, '-', color = 'b')
plt.plot(R, X_01, '-', color = 'g')
plt.grid(True)
plt.show()
