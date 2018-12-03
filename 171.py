#-*- coding: utf-8 -*-
from scipy.special import j1

def f(x):
    return j1(2*x)

a = 0
b = 10

funa = f(a)
funb = f(b)

if ( funa * funb > 0.0):
    print "Dotajaa intervaalaa [%s, %s] saknju nav"%(a,b)
    sleep(1); exit()
else:
    print "Dotajaa intervaalaa sakne(s) ir!"

deltax = 0.0001

while ( fabs(b-a) > deltax ):
    x = (a+b)/2; funx = f(x)
    if ( funa*funx < 0. ):
        b = x
    else:
        a = x
print "Funkcijas saknes vertiba ir: ", x
