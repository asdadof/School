from pylab import *

m = 0.66          # massen av gjenstanden, kg
k = 1.31*10**(-3)    # luftmotstandstallet, kg/m
g = 9.81             # tyngdeakselerasjon, m/s^2
v0 = 5.05         # startfart, m/s
y0 = 1.02           # starthøyde, m
theta = radians(72)  # konverterer vinkelen til radianer

# Konstante krefter
G = array([0, -m*g]) # tyngden i N

# Variable krefter, utregning av kraftsum og akselerasjon
def a(v):                  # akselerasjonsfunksjon
  e_v = v/norm(v)          # enhetsvektor for farten
  L = -k*norm(v)**2 * e_v  # luftmotstandsvektor, N
  sum_F = G + L            # vektorsummen av kreftene, N
  aks = sum_F/m            # akselerasjonsvektoren, m/s^2
  return aks

# Startverdier for bevegelsen
r = array([0, y0])                         # startposisjon, m
v = array([v0*cos(theta), v0*sin(theta)])  # startfart, m/s
t = 0                                      # starttid, s

# Lister for lagring av verdier
r_liste = [r]
v_liste = [v]

# Simulering av bevegelsen
dt = 0.001         # tidssteg i simuleringen, s

while r[1] >= 0:   # stopper når y = 0
  v = v + a(v)*dt  # regner ut neste fartsvektor
  r = r + v*dt     # regner ut neste posisjonsvektor
  t = t + dt       # går til neste tidspunkt

  # Lagring av 2D-verdier i lister
  r_liste = concatenate([r_liste, [r]])
  v_liste = concatenate([v_liste, [v]])

print((r_liste[-1]-0.1)*0.95)