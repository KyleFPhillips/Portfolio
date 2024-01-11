# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 00:56:49 2023

@author: kp503
"""
#Section 1: without stimulus, same as fig 5B

import matplotlib.pyplot as plt
import numpy as np

from enum import Flag

class Siphon(Flag):
    on = True
    off = False
    
fig, ax = plt.subplots(dpi=144)
h_min = 0.15
a_c = 0.0144
a_s = 0
s_period = 1
phase = 0
phase = np.floor(phase/s_period)
b = 0.9
numstep = 109
periods = 5
h_n_last = 0.2 + a_c
h_n_last2 = 0.2
n_range = np.arange(2, numstep * 2 + 1)
h_arr = np.empty(len(n_range))
siphon = Siphon.off

for i,n in enumerate(n_range):
    test_n = np.floor((n-phase)/s_period) - (n-phase)/s_period
    if np.isclose(test_n, 0):
        a = a_c + a_s
        
    else:
        a = a_c
        
    if h_n_last < h_min or (h_n_last - h_n_last2 > 0 and not siphon):
        siphon = Siphon.off
        if a+h_n_last < 1:
            h_n=h_n_last + a
        else:
            h_n = 1
            siphon = Siphon.on
            
    elif n > 2 and siphon and h_n_last > h_min: 
        h_n = np.min([a + b * h_n_last, 1])
    
    else:
        h_n = 1
        print('Unexpected Result!')
        
    h_n_last2 = h_n_last
    h_n_last = h_arr[i] = h_n

ax.plot(n_range, h_arr, 'r-')
ax.axhline(h_min, ls='--',color='gray')
ax.set_xlabel('Number of Timesteps')
ax.set_ylabel('Height of Water in Cup')
ax.set_title(f'Tantalus cup model with stimulus period {s_period} and stimulus amplitude {a_s}')
plt.show()

#%%

#Section 2: with stimulus


import matplotlib.pyplot as plt
import numpy as np

from enum import Flag

class Siphon(Flag):
    on = True
    off = False
    
fig, ax = plt.subplots(dpi=144)
h_min = 0.15
a_c = 0.0144
a_s = 0.3
s_period = 12
phase = 0
phase = np.floor(phase/s_period)
b = 0.9
numstep = 109
periods = 5
h_n_last = 0.2 + a_c
h_n_last2 = 0.2
n_range = np.arange(2, numstep * 2 + 1)
h_arr = np.empty(len(n_range))
siphon = Siphon.off

for i,n in enumerate(n_range):
    test_n = np.floor((n-phase)/s_period) - (n-phase)/s_period
    if np.isclose(test_n, 0):
        a = a_c + a_s
        
    else:
        a = a_c
        
    if h_n_last < h_min or (h_n_last - h_n_last2 > 0 and not siphon):
        siphon = Siphon.off
        if a+h_n_last < 1:
            h_n=h_n_last + a
        else:
            h_n = 1
            siphon = Siphon.on
            
    elif n > 2 and siphon and h_n_last > h_min: 
        h_n = np.min([a + b * h_n_last, 1])
    
    else:
        h_n = 1
        print('Unexpected Result!')
        
    h_n_last2 = h_n_last
    h_n_last = h_arr[i] = h_n

ax.plot(n_range, h_arr, 'r-')
ax.axhline(h_min, ls='--',color='gray')
ax.set_xlabel('Number of Timesteps')
ax.set_ylabel('Height of Water in Cup')
ax.set_title(f'Tantalus cup model with stimulus period {s_period} and stimulus amplitude {a_s}')
plt.show()

#%%

#Section 3: fig 6B

import matplotlib.pyplot as plt
import numpy as np
from enum import Flag

class Siphon(Flag):
    on = True
    off = False

y_axis = []
x_axis2 = []

for amplitude in range (1,1001):
    rotationnumbers = []
    for s_period in range (1,101):
        h_min = 0.15
        a_c = 0.0144
        a_s = amplitude/1000
        phase = 0
        phase = np.floor(phase/s_period)
        b = 0.9
        numstep = 1000
        h_n_last = 0.2 + a_c
        h_n_last2 = 0.2
        n_range = np.arange(2, numstep * 2 + 1)
        h_arr = np.empty(len(n_range))
        siphon = Siphon.off
    
        for i,n in enumerate(n_range):
            test_n = np.floor((n-phase)/s_period) - (n-phase)/s_period
            if np.isclose(test_n, 0):
                a = a_c + a_s
        
            else:
                a = a_c
            
            if h_n_last < h_min or (h_n_last - h_n_last2 > 0 and not siphon):
                siphon = Siphon.off
                if a+h_n_last < 1:
                    h_n=h_n_last + a
                else:
                    h_n = 1
                    siphon = Siphon.on
            
            elif n > 2 and siphon and h_n_last > h_min:
                h_n = np.min([a + b * h_n_last, 1])
        
            else:
                h_n = 1
                print('Unexpected Result!')
    
            h_n_last2 = h_n_last
            h_n_last = h_arr[i] = h_n
        
        
        #Creates an array of numbers to label each individual timestep
        h_numbers = np.arange(len(h_arr))
        #Filters the timestep numbers which are less than h_min, 
        #indicating a finished cycle
        cycle_resets = h_numbers[h_arr<0.15]
        #If cycle_resets is empty, it indicates a cycle that never ends
        if len(cycle_resets) == 0: 
            #If a cycle lasts indefinitely, its rotation number is 0
            rotationnumbers = np.append(rotationnumbers, 0) 
        else:
            #If a cycle has a finite length, the length is calculated
            difference = cycle_resets[-1]-cycle_resets[-2]
            #The rotation number is calculated from the ratio of period 
            #to cycle length
            rotation = s_period/difference
            #The rotation number is recorded in an array for later
            rotationnumbers = np.append(rotationnumbers, rotation)
            
        #Cleaning the data slightly to avoid a spiked graph
    for i in range (1,100): 
        if rotationnumbers[i]<rotationnumbers[i-1]:
            rotationnumbers[i] = rotationnumbers[i-1]
    
    points = np.zeros(len(rotationnumbers))
    
    for i in range (1,100):
        if rotationnumbers[i] != rotationnumbers[i-1]:
            points[i] = 1
    
    for i in range (1,100):
        if points[i] != 0:
            x_axis2 = np.append(x_axis2, i+1)
    
    for i in range (1,100):
        if points[i] != 0:
            y_axis = np.append(y_axis, points[i]*a_s)
            
    print(amplitude) #Gives an indication of the program's progress

fig, ax = plt.subplots(dpi=144)
ax.set_xlabel('Forcing period')
ax.set_ylabel('Forcing amplitude')
ax.set_title('6B: Graph relating changes in rotation number to timestep and amplitude')

#s=1 is used to reduce the size of each point for easier viewing
plt.scatter(x_axis2, y_axis, s=1)
plt.show()
