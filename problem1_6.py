'''Evolve a grid of initial conditions for standard map, each for 1000 steps.'''

import matplotlib.pyplot as plt
import numpy as np

# Time steps
dt = 0.01
t_0 = 0
t_f = 10
n_steps = int((t_f - t_0) / dt)


# Initialize variables and parameters
theta_arr = np.zeros(n_steps+1)
v_arr = np.zeros(n_steps+1)
theta_arr[0] = 1
v_arr[0] = 1
k = 1


# Start plot
fig, axs = plt.subplots(2, 3)

axsDict = {1: axs[0, 0], 2: axs[0, 1], 3: axs[0, 2], 4: axs[1, 0], 5: axs[1, 1], 6: axs[1, 2]}
for k in range(1, 7):

    # Grid of initial conditions
    for x in range(10):
        theta_arr[0] = x
        
        for y in range(10):
            v_arr[0] = y
            
            # Euler's method
            for i in range(1, n_steps+1):
                theta = theta_arr[i-1]
                v = v_arr[i-1]
                
                theta_arr[i] = theta + v + k*np.sin(theta)
                v_arr[i] = v + k*np.sin(theta)
            axsDict[k].plot(theta_arr, v_arr)
            plt.xlabel('Theta')
            plt.ylabel('V')
            

# Plot results
plt.show()

'''This shows that the Standard Map has a mixed state space.'''
