# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 15:59:04 2020

@author: Himanshu Tyagi
"""

from scipy.integrate import solve_ivp
def f(x, y): 
    return [32*y[0] + 66*y[1] + (2/3)*x + 2/3 , -66*y[0] - 133*y[1]-(1/3)*x - (1/3) ]
sol = solve_ivp(f, (0, 0.5), [1/3, 1/3])
xs= sol.t
ys= sol.y
import matplotlib.pyplot as plt
plt.plot(xs, ys[0], label=('$y_1$'))
plt.plot(xs, ys[1], label=('$y_2$'))
plt.xlabel('$x$')
plt.ylabel('$y_1$ &  $y_2$')
plt.legend()
plt.show()

##It is clear from the differential equations that change in y2 is almost -2 times y1
##Hence for same initial values the plots shows the correct results