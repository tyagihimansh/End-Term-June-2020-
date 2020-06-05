# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 17:17:27 2020

@author: Himanshu Tyagi
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as int
def f(x,y):   
    return(np.vstack([y[1], 4*(y[0] - x)]))
def bcf(ya,yb):                 
    return(np.array([ya[0],yb[0]-2]))
x=np.linspace(0,1,100)           
y=np.zeros([2,len(x)]) 
res= int.solve_bvp(f, bcf, x, y)
plt.subplot(221)
plt.plot(x, res.sol(x)[0], label='y(x)')
plt.legend()
def correct_sol(x):
    return x+ np.exp(2)*((np.exp(4)-1)**(-1))*(np.exp(2*x)-np.exp(-2*x))
plt.subplot(222)
plt.plot(x, correct_sol(x), label= 'Analytical')
plt.legend()
error= (res.sol(x)[0]-correct_sol(x))*100/correct_sol(x)
print(error)
plt.subplot(223)
plt.subplots_adjust(hspace= 0.5)
plt.plot(x, error, label= 'Relative Error')
plt.legend()
plt.show()