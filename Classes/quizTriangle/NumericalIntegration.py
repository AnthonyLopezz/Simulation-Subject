#Brian Rodriguez

import random
import numpy as np
import matplotlib.pyplot as plt


functionf = lambda x: (x - 1)
functiong = lambda x: (-x + 13)

a = 1
b = 7

m = 7
n = 13

NumSteps = 100000
XIntegral = []
YIntegral = []
XRectangle = []
YRectangle = []

ymin = functionf(a)
ymax = ymin
for i in range(NumSteps):
    x = a + (b - a) * float(i) / NumSteps
    y = functionf(x)
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
    if y <= functionf(x):
        M += 1
        XIntegral.append(x)
        YIntegral.append(y)
    else:
        XRectangle.append(x)
        YRectangle.append(y)
NumericalIntegral1 = M / N * A

ymin = functiong(0)
ymax = ymin
for i in range(NumSteps):
    x = m + (n - m) * float(i) / NumSteps
    y = functiong(x)
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
    if y <= functiong(x):
        M += 1
        XIntegral.append(x)
        YIntegral.append(y)
    else:
        XRectangle.append(x)
        YRectangle.append(y)
NumericalIntegral2 = M / N * A
print('First triangle area = ' + str(NumericalIntegral1))
print('Second triangle area = ' + str(NumericalIntegral2))
totalArea = NumericalIntegral1 + NumericalIntegral2
print('Total area = ' + str(totalArea))

XLin = np.linspace(a, b)
YLin = []
for x in XLin:
    YLin.append(functionf(x))
plt.axis([1, b, 0, functionf(b)])
plt.plot(XLin, YLin, color='red', linewidth='4')
plt.scatter(XIntegral, YIntegral, color='blue', marker='.')
plt.scatter(XRectangle, YRectangle, color='yellow', marker='.')
plt.title('Function f(x)')
plt.show()

XLin = np.linspace(m, n)
YLin = []
for x in XLin:
    YLin.append(functiong(x))
plt.axis([7, 13, functiong(n), 6])
plt.plot(XLin, YLin, color='red', linewidth='4')
plt.scatter(XIntegral, YIntegral, color='blue', marker='.')
plt.scatter(XRectangle, YRectangle, color='yellow', marker='.')
plt.title('Funtion g(x)')
plt.show()
