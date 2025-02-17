import math

retning = math.pi / 4
neste_retning = math.pi/2

x=0
y=0
P=[x,y]
Distance = 1000



while Distance > 0.001:
    P[0] += math.cos(retning) * Distance
    P[1] += math.sin(retning) * Distance
    Distance /= 2
    retning -= neste_retning

print(P)


