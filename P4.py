# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 14:08:03 2020

@author: Himanshu Tyagi
"""

import numpy as np
import numpy.fft as fft
import matplotlib.pyplot as plt
sample= np.random.rand(1024)
x= np.arange(len(sample))
"""a"""
plt.scatter(x, sample, s= 0.5)
plt.title('Random Number Distribution')
plt.show()
"""b"""
ft = fft.fftshift(fft.fft(sample))  
k = 2*np.pi*fft.fftshift(fft.fftfreq(len(sample),1))
power_spectrum = (np.abs(ft)**2)/(len(ft)*2*np.pi)
plt.plot(k, power_spectrum)
plt.title('Power Spectrum')
plt.show()
"""c""" """The minimum and maximum value of k depends on the value of the dx so 
for different step size wavevector will change hence the minimum and maximum as well."""

"""d"""
from scipy import stats
k_bin, pdg_bin, binnumber= stats.binned_statistic(k, power_spectrum, bins= 5)
av_pdg_bin=(pdg_bin[0:len(pdg_bin)-1]+pdg_bin[1:len(pdg_bin)])/2
plt.bar(av_pdg_bin, k_bin, width=pdg_bin[1]-pdg_bin[0])
plt.title('Power Spectrum')
plt.show()

"""e""" """As my distribution is unideviate, hence it was expected that Fourier
Transform of a constant function will give me a delta function"""