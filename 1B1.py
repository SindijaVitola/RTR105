import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import *
x = linspace(0, 7, 70)
y = cos(x)

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $cos(x)$ un $sin(x)$')
plt.plot(x, y)         
plt.plot(x, y, color = "#007F00")


y2 = sin(x)
plt.plot(x,y2, color = "#FF0000")

plt.legend(['$cos(x)$','$sin(x)$'])

plt.show()
