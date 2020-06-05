# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 18:14:47 2020

@author: Himanshu Tyagi
"""
import numpy as np
import numpy.fft as fft
import matplotlib.pyplot as plt
def f(x):
    f = np.zeros(len(x))
    for i in range(len(x)):
        if x[i] < 1 and x[i] > -1:
            f[i] = 1
        else:
            f[i] = 0
    return f
n = 4096
x = np.linspace(-50, 50, n+1)
plt.plot(x, f(x))
plt.title('Box function')
plt.show()
dx= x[1]-x[0]
y = f(x[0:n])
y = fft.fftshift(y)           
dft = fft.fftshift(fft.fft(y))
k = 2*np.pi*fft.fftshift(fft.fftfreq(n,dx)) 
ft = ((dx)/np.sqrt(2*np.pi))*np.real(dft)
plt.subplot(221)
plt.plot(k, ft)
plt.title('Fourier Transform of Box function')
n1 = 2048
x1 = np.linspace(-50, 50, n1+1)
dx1= x1[1]-x1[0]
y1 = f(x1[0:n1])
y1 = fft.fftshift(y1)           
dft1 = fft.fftshift(fft.fft(y1))
k1 = 2*np.pi*fft.fftshift(fft.fftfreq(n1,dx1)) 
ft1 = ((dx)/np.sqrt(2*np.pi))*np.real(dft1)
plt.subplot(222)
plt.plot(k1, ft1)
plt.title('Fourier Transform of Box function')
n2 = 512
x2 = np.linspace(-50, 50, n2+1)
dx2= x2[1]-x2[0]
y2 = f(x2[0:n2])
y2 = fft.fftshift(y2)           
dft2 = fft.fftshift(fft.fft(y2))
k2 = 2*np.pi*fft.fftshift(fft.fftfreq(n2,dx2)) 
ft2 = ((dx)/np.sqrt(2*np.pi))*np.real(dft2)
plt.subplot(223)
plt.plot(k2, ft2)
plt.title('Fourier Transform of Box function')
plt.show()