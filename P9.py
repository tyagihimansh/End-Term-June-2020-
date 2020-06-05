# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 19:53:31 2020

@author: Himanshu Tyagi
"""

import numpy as np
A= np.array([[2,1 ], [1, 0], [0, 1]])
B= np.array([[1, 1, 0], [1, 0, 1], [0, 1, 1]])
l=np.linalg.svd(A)
m= np.linalg.svd(B) 
print('singular values of A',l[1])
print('singular values of B', m[1])