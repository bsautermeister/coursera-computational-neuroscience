"""
@author: bsautermeister

Quiz 2 code.
"""

import numpy as np
import matplotlib.pyplot as plt

import pickle

from week2.compute_sta import compute_sta

FILENAME = 'c1p8.pickle'

with open(FILENAME, 'rb') as f:
    data = pickle.load(f)

# values are downsampled to delta_t = 2ms
stim = data['stim']
rho = data['rho']

# Fill in these values
sampling_period = 2  # in ms
num_timesteps = int(300 / sampling_period)  # 300ms

sta = compute_sta(stim, rho, num_timesteps)

time = (np.arange(-num_timesteps, 0) + 1) * sampling_period

plt.plot(time, sta)
plt.xlabel('Time (ms)')
plt.ylabel('Stimulus')
plt.title('Spike-Triggered Average')

plt.show()
