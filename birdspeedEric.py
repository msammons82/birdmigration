#!/usr/bin/env python 3
# Visualize 2D speed vs Frequency for the gull 
# named "Eric"
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

birddata = pd.read_csv("C:/Users/micha/Documents/Python Learning/bird_tracking.csv")
bird_names = pd.unique(birddata.bird_name)

# storing the indices of the bird Eric
ix = birddata.bird_name == "Eric"
speed = birddata.speed_2d[ix]

plt.figure(figsize = (8,4))
ind = np.isnan(speed)
plt.hist(speed[~ind], bins = np.linspace(0,30,20), density = True, stacked = True)
plt.xlabel(" 2D speed (m/s) ")
plt.ylabel(" Frequency ")
plt.show()