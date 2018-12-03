# Fails: 170.py
#Autors:...................
#Apliecibas numurs:.................
#Datums:........
#Sagatave funkcijas saknes mekleeshanai ar dihatomijas metodi

#-*- coding: utf-8 -*-
from math import sin, fabs
from time import sleep

def f(x):
    return sin(x)

a = 1.1
b = 3.2

funa = f(a)
funb = f(b)

if ( funa * funb > 0.0):
    print "Dotajaa intervaalaa [%s, %s] saknju nav"%(a,b)
    sleep(1); exit()
else:
    print "Dotajaa intervaalaa sakne(s) ir!"

deltax = 0.01
k = 0
while ( fabs(b-a) > deltax ):
    k = k + 1
    x = (a+b)/2; funx = f(x)
    if ( funa*funx < 0. ):
        b = x
    else:
        a = x
print "Sakne ir: ", x
print"Dotās funkcijas vērtība šajā punktā: ", f(x)
print"Nepieciešamo iterāciju skaits intervālu dalīšanai uz pusēm: ", k

