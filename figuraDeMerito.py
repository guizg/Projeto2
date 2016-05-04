# -*- coding: utf-8 -*-
"""
Created on Wed May  4 10:43:43 2016

@author: GuilhermeZaborowsky
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

Tn = []

for e in T:
    Tn.append(e+2)

#constantes, Y = [C, S]

C0lista = []

for i in range(100):
    C0lista.append(i*80000)

def k2(Y, t):
    k2 = 0.55 *(1+((Y[1]*0.1)/0.68)) - 0.02*t
    return k2

k1 = 0.0016
km = 0.2
Smax = []


def func(Y,t):
    dCdt = -k1*Y[0] - km*Y[0]
    dSdt = k1*Y[0] - k2(Y, t)*Y[1]
    return [dCdt, dSdt]

for i in range(100):

    S0 = 0
    Y0 = [C0lista[i], S0]

    Y = odeint(func,Y0,T)
    
    Smax.append(max(Y[:,1]))

Constante = [152]*100
Constante2 = [3.2]*100
Weedlista =[0]
for i in range (99):
    Weedlista.append (Weedlista[i] + 0.143)
print (Weedlista[23])

plt.plot(Weedlista,Constante, 'r', lw = 1, linestyle = '--')
plt.plot(Constante2,Smax, 'b', lw = 1, linestyle = '--')
plt.plot(Weedlista,Smax,'g', lw = 2.5)
plt.axis([0, max(Weedlista), 0, max(Smax)])
plt.ylabel('Pico de concentração no sangue (ng/ml)')
plt.xlabel('Qtade de maconha no brigonha (g)')
plt.title(r'')
plt.show()




