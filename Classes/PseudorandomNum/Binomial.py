import numpy as np
import matplotlib.pyplot as plt
N = 1000     # Amount of the random numbers.
n = 10       # Random Upper Limit
p = 0.5      # Probability density
P1 = np.random.binomial(n, p, N) #Generating binomial random numbers
plt.plot(P1)    #Plotting the random numbers 
plt.show()

plt.figure()    #Plotting the PDF 
plt.hist(P1, density=True, alpha=0.8, histtype='bar', color='yellow', ec='black')
plt.show()      #We hope a bell plotting