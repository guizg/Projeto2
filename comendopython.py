# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 14:00:28 2016

@author: bvbit
"""

from scipy.integrate import odeint
import matplotlib.pyplot as plt
from numpy import linspace


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

Tlista = linspace(0,13.547722,100)

# Modelo, Y = [ E , C]
k = 2
ke = 7

def func2(Y,t):
    dEdt = -ke*Y[0]
    dCdt = ke*Y[0] - k*Y[1]
    return [dEdt, dCdt]

# Condição Inicial
C0 = 0.0
E0 = 1 
Y0 = [E0, C0]

# Realiza  a integração numérica
Y = odeint(func2,Y0,Tlista)

plt.plot(T,Cexp)
plt.plot(Tlista,Y[:,0],'g')
plt.plot(Tlista,Y[:,1],'r')
plt.axis([0, max(T), 0, max(Cexp)])
plt.ylabel('Concentração (g/L)')
plt.xlabel('Tempo (h)')
plt.title('Dados Experimentais')
plt.show()

