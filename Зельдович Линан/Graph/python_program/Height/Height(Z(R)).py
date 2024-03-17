import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.animation import FuncAnimation
from scipy.optimize import curve_fit
from scipy.optimize import fsolve



def func(x, k, b):
    return k*x**b


data_1 = np.loadtxt("../../../Data/Height/Z/Le_F = 1, Le_X = 1, R = 0.005, q = 0.9, sigma = 0.15.txt")
data_2 = np.loadtxt("../../../Data/Height/Z/Le_F = 1, Le_X = 1, R = 0.1, q = 0.9, sigma = 0.15.txt")
data_3 = np.loadtxt("../../../Data/Height/Z/Le_F = 1, Le_X = 1, R = 1, q = 0.9, sigma = 0.15.txt")


X_1 = data_1[:, 0]
Z_1 = data_1[:, 2]

X_2 = data_2[:, 0]
Z_2 = data_2[:, 2]

X_3 = data_3[:, 0]
Z_3 = data_3[:, 2]



R = 0.005
q = 0.9
sigma = 0.15
Le_X = 1
Le_F = 1

dot_cnt = 100
Z = np.linspace(5, 15, dot_cnt)
X_0_1 = np.linspace(5, 15, dot_cnt)
X_0_2 = np.linspace(5, 15, dot_cnt)
X_0_3 = np.linspace(5, 15, dot_cnt)


def amp(R):
    return Le_X*Le_F/(2*R*(1-sigma)**2)

def func_1(x):
    return 2*x + Le_X*(1 - x)

def func_2(x):
    return q*(1 - sigma)*x*(1 + x)

def func(x, z):
    return amp(R)*np.exp(z*func_2(x)/(func_2(x) - func_1(x))) - x/(1-x)**2


for i in range(0, len(Z), 1):
    
    
    R = 0.005
    X_0_1[i] = fsolve(func, 0.5, Z[i])
    
    R = 0.1
    X_0_2[i] = fsolve(func, 0.5, Z[i])
    
    R = 1
    X_0_3[i] = fsolve(func, 0.5, Z[i])
    






fig = plt.figure()

plt.grid(True)




plt.plot(Z_1, X_1, '-', color = 'r')
plt.plot(Z_2, X_2, '-', color = 'g')
plt.plot(Z_3, X_3, '-', color = 'b')

plt.plot(Z, X_0_1, '-.', color = 'r')
plt.plot(Z, X_0_2, '-.', color = 'g')
plt.plot(Z, X_0_3, '-.', color = 'b')



