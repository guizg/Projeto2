# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 11:09:26 2016

@author: Clearly Not Beit El
"""

from scipy.integrate import odeint
import matplotlib.pyplot as plt


T = [0,
2.0223916,
5.01462,
7.0135713,
11.525331,
13.547722]

Cexp = [0,
0.003532348,
0.67059183,
0.54666984,
0.005038931,
0.001506583]

#constantes, Y = [C, S]

k1 = 0.0018
k2 = 0.55
km = 0.20


def func(Y,t):
    dCdt = -k1*Y[0] - km*Y[0]
    dSdt = k1*Y[0] - k2*Y[1]
    return [dCdt, dSdt]

C0 = 500
S0 = 0
Y0 = [C0, S0]

Y = odeint(func,Y0,T)

Tn = []

for e in T:
    Tn.append(e+2)

Y2=[]

for e in Y[:,1]:
    Y2.append((e -0.2))

plt.plot(T, Cexp)
plt.plot(T, Cexp,'bo')
plt.plot(Tn,Y[:,0],'g')
plt.plot(Tn,Y2,'r')
plt.axis([0, max(T), 0, max(Cexp)+1])
plt.ylabel('Concentração (ng/ml)')
plt.xlabel('Tempo (min)')
plt.title(r'Dados Experimentais')
plt.show()