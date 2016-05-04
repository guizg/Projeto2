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

for i in range(10):
    C0lista.append(i*100)


k1 = 0.0017
k2 = 0.51
km = 0.38
Smax = []

def func(Y,t):
    dCdt = -k1*Y[0] - km*Y[0]
    dSdt = k1*Y[0] - k2*Y[1]
    return [dCdt, dSdt]


for i in range(10):

    S0 = 0
    Y0 = [C0lista[i], S0]

    Y = odeint(func,Y0,T)
    
    Smax.append(max(Y[:,1]))
    


plt.plot(C0lista,Smax,'g')
plt.axis([0, max(C0lista), 0, max(Smax)])
plt.ylabel('Pico de concentração no sangue (ng/ml)')
plt.xlabel('Concentração Inicial no Estomago (ng/ml)')
plt.title(r'Dados Experimentais')
plt.show()




