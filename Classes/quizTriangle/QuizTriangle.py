#Anthony Jardiel López Pérez || 2271557

import random
import numpy as np
import matplotlib.pyplot as plt


f = lambda x: (x - 1)
g = lambda x: (-x + 13)

a = 1
b = 7

m = 7
n = 13

NumSteps = 100000
XIntegral = []
YIntegral = []
XRectangle = []
YRectangle = []

#First function f(x)
ymin = f(a)
ymax = ymin
for i in range(NumSteps):
    x = a + (b - a) * float(i) / NumSteps
    y = f(x)
    if y < ymin:
        ymin = y
    if y > ymax:
        ymax = y
A = (b - a) * (ymax - ymin)
N = 100000
M = 0
for k in range(N):
    x = a + (b - a) * random.random()
    y = ymin + (ymax - ymin) * random.random()
    if y <= f(x):
        M += 1
        XIntegral.append(x)
        YIntegral.append(y)
    else:
        XRectangle.append(x)
        YRectangle.append(y)
NumericalIntegralF = M / N * A
print('Numerical integration function f(x) = ' + str(NumericalIntegralF))

#Second function g(x)
ymin = g(0)
ymax = ymin
for i in range(NumSteps):
    x = m + (n - m) * float(i) / NumSteps
    y = g(x)
    if y < ymin:
        ymin = y
    if y > ymax:
        ymax = y
A = (n - m) * (ymax - ymin)
N = 1000000
M = 0
for k in range(N):
    x = m + (n - m) * random.random()
    y = ymin + (ymax - ymin) * random.random()
    if y <= g(x):
        M += 1
        XIntegral.append(x)
        YIntegral.append(y)
    else:
        XRectangle.append(x)
        YRectangle.append(y)
NumericalIntegralG = M / N * A
print('Numerical integration function g(x) = ' + str(NumericalIntegralG))


#Total area

TotalIntegral = NumericalIntegralF + NumericalIntegralG
print('Total Numerical integration Triangle by both functions = ' + str(TotalIntegral))

#So, this is the graph for the first function f(x)
XLin = np.linspace(a, b)
YLin = []
for x in XLin:
    YLin.append(f(x))
plt.axis([1, b, 0, f(b)])
plt.plot(XLin, YLin, color='lightskyblue', linewidth='4')
plt.scatter(XIntegral, YIntegral, color='lightslategray', marker='.')
plt.scatter(XRectangle, YRectangle, color='lightseagreen', marker='.')
plt.title('Numerical Integration f(x)')
plt.show()



#So, this is the graph for the second function g(x)
XLin = np.linspace(m, n)
YLin = []
for x in XLin:
    YLin.append(g(x))
plt.axis([7, 13, g(n), 6])
plt.plot(XLin, YLin, color='lightskyblue', linewidth='4')
plt.scatter(XIntegral, YIntegral, color='lightslategray', marker='.')
plt.scatter(XRectangle, YRectangle, color='lightseagreen', marker='.')
plt.title('Numerical Integration g(x)')
plt.show()
