import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import *
x = linspace(0, 4, 70)
y = sin(x)

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $sin(x)$')
plt.plot(x, y, color = "#0000FF")

y1 = x
plt.plot(x, y1, color = "#FF0000")

y2 = x-x**3/(2*3)
plt.plot(x, y2, color = "#00FF00")

y3 = x-x**3/(2*3)+x**5/(2*3*4*5)
plt.plot(x, y3, color = "#094FA0")

y4 = x-x**3/(2*3)+x**5/(2*3*4*5)-x**7/(2*3*4*5*6*7)
plt.plot(x, y4, color = "#A0EF00")

plt.show()
