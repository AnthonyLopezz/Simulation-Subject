import math
import random
import numpy as np
import matplotlib.pyplot as plt

N = 100000
M = 0
XCircle = []
YCircle = []
XSquare = []
YSquare = []

for p in range(N):
    x = random.random()
    y = random.random()
    if (x**2 + y**2 <= 1):
        M += 1
        XCircle.append(x)
        YCircle.append(y)
    else:
        XSquare.append(x)
        YSquare.append(y)

Pi = 4 * M / N
print('N=%d M=%d Pi=%.2f' % (N, M, Pi))


XLin = np.linspace(0, 1)
YLin = []
for x in XLin:
    YLin.append(math.sqrt(1 - x**2))
plt.axis('equal')
plt.grid(which='major')
plt.plot(XLin, YLin, color='Teal', linewidth='4')
plt.scatter(XCircle, YCircle, color='DarkCyan', marker='.')
plt.scatter(XSquare, YSquare, color='LightSeaGreen', marker='.')
plt.title('Monte Carlo method for Pi estimation')
plt.show()

