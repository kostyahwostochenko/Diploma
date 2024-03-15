import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.animation import FuncAnimation

temp = np.loadtxt("../../Data/Current/Temp Z = 9, Le_F = 1, Le_X = 1, R = 1, q = 0.9, sigma = 0.15.txt")
X = np.loadtxt("../../Data/Current/X Z = 9, Le_F = 1, Le_X = 1, R = 1, q = 0.9, sigma = 0.15.txt")
Y = np.loadtxt("../../Data/Current/Y Z = 9, Le_F = 1, Le_X = 1, R = 1, q = 0.9, sigma = 0.15.txt")
#W = np.loadtxt("../Data/Current/W Z = 9, Le_F = 1, Le_X = 1, R = 1, q = 0.9, sigma = 0.15.txt.txt")
gif = np.loadtxt("../../Data/Current/Gif.txt")
params = np.loadtxt("../../Data/Current/Params.txt")

'''
Z = params[0]
Le_F = params[1]
Le_X = params[2]
R = params[3]
q = params[4]
sigma = params[5]

Z_str = "Z = " + str(Z) + ", "
Le_F_str = "Le_F = " + str(Le_F) + ", "
Le_X_str = "Le_x = " + str(Le_X) + ", "
R_str = "R = " + str(R) + ", "
q_str = "q = " + str(q) + ", "
sigma_str = "sigma = " + str(sigma)
txt_str = ".txt"

path = Z_str + Le_F_str + Le_X_str + R_str + q_str + sigma_str + txt_str
'''


L = gif[0]
dx = gif[1]
frames_cnt = int(gif[2])
#L = 700
#dx = 0.1

x = np.arange(0, L + dx, dx)
#num = np.arange(0, 10000 + 1, 10)

fig = plt.figure()

def update_plot(frame):
    
    plt.cla()
    plt.plot(x, temp[frame,:], color = 'b')
    plt.plot(x, X[frame,:], color = 'r')
    plt.plot(x, Y[frame,:], color = 'y')
    
    #plt.legend(['temp','X','Y'], loc = 'center left')
    
    #plt.plot(x, w[frame,:], color = 'g')
    plt.xlabel('x')
    plt.ylabel('T')
    plt.title('frames ' + str(frame))
    plt.xlim([0, L])
    #plt.ylim([0, 1.8])

    plt.grid()
 
    
# Посмотреть срез в какой-то момент времени

#update_plot(100) 


#np.savetxt("../../Data/Config/Temp.txt", temp[100,:].reshape(1,-1))
#np.savetxt("../../Data/Config/X.txt", X[100,:].reshape(1,-1))
#np.savetxt("../../Data/Config/Y.txt", Y[100,:].reshape(1,-1))


X_max = np.max(X, axis = 1)
ind_max = np.argmax(X, axis = 1)
theta_0 = []

for i in range(len(ind_max)):
    theta_0.append(temp[i, ind_max[i]])
    

plt.plot(np.linspace(0, 100, 101), theta_0, '.')
plt.grid()


#plt.plot(np.linspace(0, 100, 101), np.max(X, axis = 1), '.')
#plt.grid()

#animation = FuncAnimation(fig, update_plot, frames = frames_cnt) 
#animation.save("../graph/graph_stable.gif", writer = 'pillow', fps = 24) 


'''
best
	upper right
	upper left
	lower left
	lower right
	right
	center left
	center right
	lower center
	upper center
	center
'''