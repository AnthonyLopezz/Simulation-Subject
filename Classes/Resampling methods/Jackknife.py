import random
import statistics as sta
import matplotlib.pyplot as plt

# Population data.
PopData = list()

# Random seed.
random.seed(5)

# Getting N-Random numbers.
for i in range(100):
    # Getting a random number between 0..100
    DataElem = 10 * random.random()
    PopData.append(DataElem)


def CVCalc(data):
    ''' Calculation of the cofficient of variation.
        data: Input data.
    '''
    CVCalc = sta.stdev(data) / sta.mean(data)
    return CVCalc

# Calculating of cofficient of variation of the population data.
CVPopData = CVCalc(PopData)
print(f'Coefficient of variation on population data:  {CVPopData}')


N = len(PopData)
JackVal = list()
PseudoVal = list()

# Initializing the jackKnife sub-sampling with 0-value.
for i in range(N - 1):
    JackVal.append(0)

# Initializing the Pseudo valules sub-sampling with 0-value.
for i in range(N):
    PseudoVal.append(0)

# Looping for N-Pseudo values.
for i in range(N):
    # Looping for N-1 sub-sampling items.
    for j in range(N):
        if (j < i):
            JackVal[j] = PopData[j]
        else:
            if (j > i):
                JackVal[j - 1] = PopData[j]
    # Calculating the dispersion of the CV* with resampling-CV
    PseudoVal[i] = N * CVCalc(PopData) - (N - 1) * CVCalc(JackVal)

# Show the population dispersion
plt.hist(PseudoVal)
plt.show()
# Show the statistics data
MeanPseudoVal = sta.mean(PseudoVal)
print(MeanPseudoVal)
VariancePseudoVal = sta.variance(PseudoVal)
print(VariancePseudoVal)
VarJack = sta.variance(PseudoVal) / N
print(VarJack)
