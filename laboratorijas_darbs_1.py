# -*- coding: utf-8 -*-
from scipy.special import j1

def mana_funkcija(x):
    k = 0
    a = (-1)**0*x**0/(1)
    S = a
    print("Izdruka no liet.f. a0 = %6.2f S0 = %6.2f"%(a,S))
    
    while k < 500:
        k = k + 1
        R = (1/(k**2+k)*(-1)*x**-2)
        a = a * R
        S = S + a
        if k == 499:
            print("Izdruka no liet.f. a%d = %6.2f S%d = %6.2f"%(k,a,k,S))
        
    S = S + a
    print("Izdruka no liet.f. a500 = %6.2f S500 = %6.2f"%(a,S))
    return S

x = float(input("Lietotāj, lūdzu, ievadi argumentu (x): "))
y = j1(2*x)
print("standarta sin(%.2f) = %6.2f"%(x,y))

yy = mana_funkcija(x)
m = u"\u221E"
print("mans sin(%.2f) = %6.2f"%(x,yy))
print("")


print("               500")
print("             _______ ")
print("            \            k   2*k ")
print("             \       (-1) * x    ")
print("j1(2*x) ~ x * >     ____________  , kur -%s<x<%s"%(m,m))
print("             /        k!*(k+1)!  ")
print("            /______  ")
print("               k=0")


print("                              1")
print("rekurences reizinātājs: _______________")
print("                          2          -2")
print("                        (k + k)*(-1)*x")
