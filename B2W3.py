#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 09:10:27 2021

@author: SamR
"""
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from scipy.integrate import quad


#ro**2 = the variance
ro = 1
#mu = is the mean value of the distribution
mu = 0

def g_X(x, alpha):
    return (1/(ro*np.sqrt(2*np.pi)))*np.exp((-1/2)*(((x-mu)**2)/ro**2))

#a = -np.inf
#b = np.inf
a = -1
b = 1
N = 100

alpha_ary = linspace(0,1,N) # create an array of values of alpha
value = zeros(N)            # create an array to store results of integrations

# do the integrations
idx = 0
for alpha in alpha_ary:
    value[idx],error = quad(g_X,a,b,args=alpha) # note use of the args optional argument
    idx = idx + 1

# plot the result
figure(1)
clf()
plot(alpha_ary,value)


xlabel(r'$\alpha$')
ylabel('Integral')
title(r"Plot of g(x)")
