import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

data_1_speed = np.loadtxt("../../Data/Speed/Z/Le_F = 0.5, Le_X = 1, R = 0.005, q = 0.9, sigma = 0.15.txt")
data_2_speed = np.loadtxt("../../Data/Speed/Z/Le_F = 1, Le_X = 1, R = 0.005, q = 0.9, sigma = 0.15.txt")
data_3_speed = np.loadtxt("../../Data/Speed/Z/Le_F = 1.5, Le_X = 1, R = 0.005, q = 0.9, sigma = 0.15.txt")

data_1_height = np.loadtxt("../../Data/Height/Z/Le_F = 0.5, Le_X = 1, R = 0.005, q = 0.9, sigma = 0.15.txt")
data_2_height = np.loadtxt("../../Data/Height/Z/Le_F = 1, Le_X = 1, R = 0.005, q = 0.9, sigma = 0.15.txt")
data_3_height = np.loadtxt("../../Data/Height/Z/Le_F = 1.5, Le_X = 1, R = 0.005, q = 0.9, sigma = 0.15.txt")


speed_1 = data_1_speed[:, 0]
Z_1 = data_1_speed[:, 1]
Height_1 = data_1_height[:, 0]

speed_2 = data_2_speed[:, 0]
Z_2 = data_2_speed[:, 1]
Height_2 = data_2_height[:, 0]

speed_3 = data_3_speed[:, 0]
Z_3 = data_3_speed[:, 1]
Height_3 = data_3_height[:, 0]

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



# Сначала передается функция, в которую подставляется x, затем его начальное
# приближение, а потом дополнительные аргументы функции func

for i in range(0, len(Z), 1):
    
    Le_F = 0.5
    X_0_1[i] = fsolve(func, 0.5, Z[i])
    
    Le_F = 1
    X_0_2[i] = fsolve(func, 0.5, Z[i])
    
    Le_F = 1.5
    X_0_3[i] = fsolve(func, 0.5, Z[i])
    
speed_a_1 = np.sqrt(4*R*X_0_1**2/(Le_X*(1 - X_0_1**2)))
speed_a_2 = np.sqrt(4*R*X_0_2**2/(Le_X*(1 - X_0_2**2)))
speed_a_3 = np.sqrt(4*R*X_0_3**2/(Le_X*(1 - X_0_3**2)))


plt.plot(Z_1, Height_1, '-', color = 'r')
plt.plot(Z_2, Height_2, '-', color = 'b')
plt.plot(Z_3, Height_3, '-', color = 'g')

plt.plot(Z, X_0_1, '--', color = 'r')
plt.plot(Z, X_0_2, '--', color = 'b')
plt.plot(Z, X_0_3, '--', color = 'g')

plt.legend(['$Le_F$ = 0.5', '$Le_F$ = 1', '$Le_F$ = 1.5'])
plt.xlabel('Z')
plt.ylabel('Height')

plt.grid(True)
plt.show()
