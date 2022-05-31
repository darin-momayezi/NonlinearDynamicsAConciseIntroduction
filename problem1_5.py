from tkinter import N
from turtle import color
'''Nonlinear Dyanmics: A Concise Introduction Problem 1.5'''

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

dt = 0.01
t_start = 0
t_end = 100
n_steps = int((t_end-t_start)/dt)
mu = 0.119
nu = 0.1
gamma = 0.9

# Define system of ODEs
x_arr = np.zeros(n_steps+1)
y_arr = np.zeros(n_steps+1)
z_arr = np.zeros(n_steps+1)
t_arr = np.zeros(n_steps+1)
t_arr[0] = t_start
x_arr[0] = 1
y_arr[0] = 1
z_arr[0] = 1

# Euler's method
for i in range(1, n_steps+1):
    x = x_arr[i-1]
    y = y_arr[i-1]
    z = z_arr[i-1]
    t = t_arr[i-1]
    dxdt = mu*x - y*z
    dydt = -1*nu*y + x*z
    dzdt = gamma - z + x*y
    
    x_arr[i] = x + dxdt*dt
    y_arr[i] = y + dydt*dt
    z_arr[i] = z + dzdt*dt
    
    t_arr[i] = t + dt
    
# Plot results
fig = plt.figure()
ax = Axes3D(fig)
ax.plot3D(x_arr, y_arr, z_arr, c='red')
ax.scatter3D(x_arr, y_arr, z_arr, 'gray')
plt.show()
