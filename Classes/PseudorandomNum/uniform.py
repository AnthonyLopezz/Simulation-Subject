import numpy as np
import matplotlib.pyplot as plt 

a = 1                               #Random Lower Limit
b = 100                             #Random Upper Limit
N = 10000                           #Amount of random number
x1 = np.random.uniform(a, b, N)     #Generating the uniform random numbers
plt.plot(x1)                        #Plottting the random numbers
plt.show()

plt.figure()                        #Plotting with PDF (Probability density Functional)
plt.hist(x1, density=True, histtype='stepfilled', alpha=0.2)
plt.show()                          #We hope a unifomr behavior