import matplotlib.pyplot as plt
import numpy as np

a = 75
c = 0
m = 2 ** (31) - 1
x = 0.1
u = np.array([])
N = 100  # number of random numbers

for i in range(N):
    x = np.mod((a * x + c), m)
    u = np.append(u, x / m)
    print(u[i])

# ...
s = 20 # number of pats
Ns = N / s  # ratio
S = np.arange(0, 1, 0.05)  # 20 subintervals-
counts = np.empty(S.shape, dtype=int)  # fails array
V = 0
for i in range(20):
    counts[i] = len(np.where((u >= S[i]) & (u < S[i] + 0.05))[0])
    V += (counts[i] - Ns) ** 2 / Ns
print("R = ", counts)
print("V = ", V)

Ypos = np.arange(len(counts))
plt.bar(Ypos, counts)
plt.show()
