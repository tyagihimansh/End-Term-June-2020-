# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 16:22:59 2020

@author: Himanshu Tyagi
"""
import numpy as np
"""for Repeatiation of seed"""
n=100; a=203; c= 203; X0=1; m=213
seed1= X0
rand1=np.zeros(n)
rand1[0]=X0
for i in range(1,n):
        rand1[i]=((a*rand1[i-1]+c)%m)
import matplotlib.pyplot as plt
x= np.arange(n)
plt.plot(x, rand1, '.')

"""for not Repeatiation of seed"""
n=100; a=203; c= 203; X1=250; m=233
seed2= X1
rand2=np.zeros(n)
rand2[0]=X1
for i in range(1,n):
        rand2[i]=((a*rand2[i-1]+c)%m)
import matplotlib.pyplot as plt
plt.plot(x, rand2, '.')
location1= np.where(rand1==seed1)
print('Location of seed in 1=',location1)
location2= np.where(rand2==seed2)
print('Location of seed in 2=',location2)
