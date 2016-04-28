# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 13:45:44 2016

@author: GuilhermeZaborowsky

"""

import matplotlib.pyplot as plt

# DADOS EXPERIMENTAIS

# Tempo (min)
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

# Concentração de THC no sangue (ng/ml)
Fexp = [0,
17.910448,
48.358208,
77.462685,
102.089554, 
114.62687,
141.49254,
149.10448,
144.62686,
152.2388,
146.86568,
126.268654,
94.477615,
77.01492,
48.80597,
]

plt.plot(T, Fexp,'bo')
plt.axis([0, max(T), 0, 155])
plt.ylabel('Concentração (ng/ml)')
plt.xlabel('Tempo (min)')
plt.title(r'Dados Experimentais')
plt.show()