# -*- coding: utf-8 -*-
"""
Created on Wed May  4 16:49:20 2016

@author: bvbit
"""
from scipy.integrate import odeint

T = [0,
1.0951375,
2.1606765,
3.1754756,
4.1902747,
5.154334,
6.1183934,
7.1331925,
8.147991,
9.061311,
10.12685,
12.105708,
15.099366,
18.143763,
22.5074,
]

k1 = 0.0016
k2 = 0.55
km = 0.2


def func(Y,t):
    dCdt = -k1*Y[0] - km*Y[0]
    dSdt = k1*Y[0] - k2*Y[1]*(1+((Y[1]*0.1)/0.68)) -0.02*t
    return [dCdt, dSdt]

C0 = 10200
S0 = 0
Y0 = [C0, S0]

Y = odeint(func,Y0,T)

Tn = []

for e in T:
    Tn.append(e+2)
    
print (max(Y[1]))