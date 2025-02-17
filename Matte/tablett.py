from pylab import *

# Konstanter
m = 0.66            # massen av gjenstanden, kg
k = 1.31*10**(-3)    # luftmotstandstallet, kg/m
g = 9.81             # tyngdeakselerasjon, m/s^2
v0 = 3.667           # startfart, m/s
y0 = 1.025           # starthøyde, m
x_target = 1.6         # ønsket avstand, m
toleranse = 0.001     # hvor nøyaktig vi må treffe ønsket avstand, m

# Konstante krefter
G = array([0, -m*g]) # tyngden i N

# Variable krefter, utregning av kraftsum og akselerasjon
def a(v):                  # akselerasjonsfunksjon
    e_v = v/norm(v)        # enhetsvektor for farten
    L = -k*norm(v)**2 * e_v  # luftmotstandsvektor, N
    sum_F = G + L          # vektorsummen av kreftene, N
    aks = sum_F/m          # akselerasjonsvektoren, m/s^2
    return aks

# Simulerer bevegelsen for en gitt vinkel theta
def simuler_kast(theta):
    # Startverdier for bevegelsen
    r = array([0, y0])                         # startposisjon, m
    v = array([v0*cos(theta), v0*sin(theta)])  # startfart, m/s
    t = 0                                      # starttid, s

    # Lister for lagring av verdier
    r_liste = [r]
    v_liste = [v]

    # Simulering av bevegelsen
    dt = 0.001         # tidssteg i simuleringen, s

    while r[1] >= 0:   # stopper når y = 0 (gjenstanden har truffet bakken)
        v = v + a(v)*dt  # regner ut neste fartsvektor
        r = r + v*dt     # regner ut neste posisjonsvektor
        t = t + dt       # går til neste tidspunkt

        # Lagring av 2D-verdier i lister
        r_liste = concatenate([r_liste, [r]])
        v_liste = concatenate([v_liste, [v]])

    return r_liste

# Finn riktig vinkel for ønsket avstand
def finn_vinkel(x_target):
    theta_min = radians(0)   # minste mulige vinkel (0 grader)
    theta_max = radians(90)  # største mulige vinkel (90 grader)

    while theta_max - theta_min > radians(0.01):  # iterer til vi har en presis vinkel
        theta = (theta_min + theta_max) / 2       # midtpunktet mellom minimum og maksimum vinkel
        r_liste = simuler_kast(theta)
        x_slutt = r_liste[-1][0]  # x-posisjonen når gjenstanden treffer bakken

        if abs(x_slutt - x_target) < toleranse:   # hvis vi er innenfor ønsket avstand, returner vinkelen
            return theta
        elif x_slutt < x_target:                  # hvis vi lander for kort, øk vinkelen
            theta_min = theta
        else:                                     # hvis vi lander for langt, senk vinkelen
            theta_max = theta

    return theta  # returner den beste vinkelen vi fant

# Kjør funksjonen for å finne vinkelen som gir ønsket avstand
theta_optimal = finn_vinkel(x_target)
print(f"Optimal vinkel for å nå {x_target} meter: {degrees(theta_optimal):.2f} grader")

# Simuler kastet med optimal vinkel og vis grafen
r_liste_optimal = simuler_kast(theta_optimal)

# Tegning av graf
plot(r_liste_optimal[:,0], r_liste_optimal[:,1])       # lager grafen
title(f"Skrått kast med luftmotstand, avstand = {x_target} m")  # tittel på grafen
xlabel("$x$ / m")                      # x-akse-tittel
ylabel("$y$ / m")                      # y-akse-tittel
grid()                                 # legger til rutenett
show()                                 # viser grafen
