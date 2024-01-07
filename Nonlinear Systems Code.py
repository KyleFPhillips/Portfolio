# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 00:56:49 2023

@author: kp503
"""
#without stimulus, same as fig 5B

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

#with stimulus


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

#aimed to look like fig 6B

import matplotlib.pyplot as plt
import numpy as np

from enum import Flag

class Siphon(Flag):
    on = True
    off = False
    
fig, ax = plt.subplots(dpi=144)
h_min = 0.15
a_c = 0.0144
a_s = 0.1
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
