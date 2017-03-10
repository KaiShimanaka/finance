# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 20:34:48 2017

@author: simnk
"""

import numpy as np
import matplotlib.pyplot as plt

x=np.arange(-3,3,0.1)
y_sin=np.sin(x)
x_rand=np.random.rand(100)*6-3
y_rand=np.random.rand(100)*6-3

plt.figure()

plt.subplot(1,1,1)

plt.plot(x,y_sin,marker='o',markersize=5,label='line')
plt.scatter(x_rand,y_rand,label='scatter')

plt.legend()

plt.grid(True)

plt.show()