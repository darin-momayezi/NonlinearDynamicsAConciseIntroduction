'''Evolve grid of ICs for various values of eta for the Fermi-Ulam map.'''

import matplotlib.pyplot as plt
import numpy as np

# Steps
n_steps =  100


# Initialize variables and ICs
u_arr = np.zeros(n_steps+1)
theta_arr = np.zeros(n_steps+1)
eta = [1, 2, 3, 4, 5, 6]
u_arr[0] = 1
theta_arr[0]= 1


# Start plot
fig, axs = plt.subplots(2, 3)
axes = [axs[0, 0], axs[0, 1], axs[0, 2], axs[1, 0], axs[1, 1], axs[1, 2]]


# Euler's method
for eta in eta:
    
    for a in range(1, 10):
        u_arr[0] = a
        
        for b in range(1, 10):
            theta_arr[0] = b
            
            for i in range(1, n_steps+1):
                u = u_arr[i-1]
                theta = theta_arr[i-1]
                
                u_arr[i] = abs(u + eta*np.sin(theta))
                theta_arr[i] = (theta + 2*np.pi / (u + eta*np.sin(theta))) % 2*np.pi
            axes[eta-1].plot(u_arr, theta_arr)
            axes[eta-1].set_title('eta={}'.format(eta))


plt.show()
