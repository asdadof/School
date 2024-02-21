import matplotlib.pyplot as plt 
from sympy import *


S = 340 

alfa = .01 

sigma = 5.67e-8 

x_list = []
jord_y_list = []
atmo_y_list = []

while alfa < 1:
    T_0, T_1 = symbols('T_0, T_1', nonnegative = True) 

    inn_jord = (S + sigma*T_1**4) 

    ut_jord = (sigma*T_0**4 + alfa*S) 

    inn_atmosfare = (sigma*T_0**4) 

    ut_atmosfare = (2*sigma*T_1**4) 

    
    l1 = Eq(inn_jord , ut_jord) 

    l2 = Eq(inn_atmosfare , ut_atmosfare) 
    
    T = solve([l1, l2])
    
    jord_temp = T[0][T_0]
    atmo_temp = T[0][T_1]

    x_list.append(alfa)
    jord_y_list.append(jord_temp)
    atmo_y_list.append(atmo_temp)
    
    alfa +=.01

plt.plot(x_list, atmo_y_list)

plt.plot(x_list, jord_y_list)

plt.show()