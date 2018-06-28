from math import radians
from numpy import linspace, cos, sin, tan
import matplotlib.pyplot as plt

g = 9.81
plt.grid(True)

V = float(input("Initial speed: "))
a = radians(int(input("Angle: ")))
h = float(input("Initial height: "))

x = linspace(0, 100)
y = -(g*x**2)/(2*V**2*cos(a)**2)+x*tan(a)+h
plt.plot(x, y)

plt.show()
