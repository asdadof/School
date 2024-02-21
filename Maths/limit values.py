'''
def f(x): 

    return 3*x - 6 

svar = input("Velg verdi for a: ") 
a = float(svar) 
t = 0.1 

while t > 0.0000001: 

    print("f(" + str(round(a - t, 7)) + ") =", round(f(a - t), 7)) 

    t = t/10 
t = 0.1 

while t > 0.0000001: 

    print("f(" + str(round(a + t, 7)) + ") =", round(f(a + t), 7)) 

    t = t/10


1, a=1   går mot 3 under og over

2, a=2 går mot 0

3, a=5 går mot 9 under og over 
'''
'''
def f(x): 

    return x**3+2*x**2 

svar = input("Velg verdi for a: ") 
a = float(svar) 
t = 0.1 

while t > 0.0000001: 

    print("f(" + str(round(a - t, 7)) + ") =", round(f(a - t), 7)) 

    t = t/10 
t = 0.1 

while t > 0.0000001: 

    print("f(" + str(round(a + t, 7)) + ") =", round(f(a + t), 7)) 

    t = t/10


1 -> 3
2 -> 16
3 -> 175
'''

'''
def f(x): 

    return x**3+2*x**2 

svar = input("Velg verdi for a: ") 
a = float(svar) 
t = 0.1 

while t > 0.0000001: 

    print("f(" + str(round(a - t, 7)) + ") =", round(f(a - t), 7)) 

    t = t/10 
t = 0.1 

while t > 0.0000001: 

    print("f(" + str(round(a + t, 7)) + ") =", round(f(a + t), 7)) 

    t = t/10


1 -> 3
2 -> 16
3 -> 45
'''
'''
def f(x): 

    return 3*x**3 + 3*2*x**2 

svar = input("Velg verdi for a: ") 
a = float(svar) 
t = 0.1 

while t > 0.0000001: 

    print("f(" + str(round(a - t, 7)) + ") =", round(f(a - t), 7)) 

    t = t/10 
t = 0.1 

while t > 0.0000001: 

    print("f(" + str(round(a + t, 7)) + ") =", round(f(a + t), 7)) 

    t = t/10


1 -> 9
2 -> 48
3 -> 525
'''