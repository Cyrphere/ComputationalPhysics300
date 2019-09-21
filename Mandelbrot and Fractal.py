#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 15:45:02 2019

@author: RaymondMZhang
"""

import math
import numpy as np
import matplotlib.pyplot as plt

points = int(input("What is the number of grid points? "))
a1, b1 = -2,2
a2, b2 = -2,2

x_set = np.linspace(a1, b1, points)
y_set = np.linspace(a2, b2, points)

n_iter = 100
something = np.zeros([points,points],float)
for i in range(points):
    #print(c_y)
    #print(z_x)
    #print(z_y)
    for j in range(points):
        #counter = 0
        print(i, j)
        #print(c_x)
        c_x, c_y, z_x, z_y = x_set[i], y_set[j], 0, 0
        for k in range(n_iter):
            absolute = math.sqrt(z_x**2+z_y**2)
            if absolute > 2:
                something[j, i] = k
                break
            #counter += 1
            #print(n, counter)
            temp1 = z_x
            temp2 = z_y
            z_x = temp1**2-temp2**2+c_x
            z_y = 2*temp1*temp2+c_y
plt.imshow(something, origin="lower", extent=[a1,b1,a2,b2], cmap = "hot")
plt.ylim([-1.0,1.0])
plt.xlim([-2.0,0.5])
plt.show()