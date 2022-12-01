import numpy as np
import matplotlib.pyplot as plt

DeadLife = 2
DeadDead = 93
LifeLife = 3
LifeDead = 2
population = 5

np.random.seed(3)
StatesData = ["Life", "Dead"]
#Lista anidada o una lista de dos dimensiones.

TransitionStates = [["LiLi", "LiDe"], ["DeDe", "DeLi"]]
TransitionMatrix = [[(LifeLife/(LifeLife+LifeDead)), (LifeDead/(LifeLife+LifeDead))],
                        [DeadLife/(DeadLife+DeadDead), DeadDead/(DeadLife+DeadDead)]]

MarkovChain = list()
NumDays = 365
TodayPrediction = StatesData[0]

for i in range(1, NumDays):

    if TodayPrediction == "Life":
        TransCondition = np.random.choice(
            TransitionStates[0], replace=True, p=TransitionMatrix[0])

        if TransCondition == "LiLi":
            pass

        else:
            TodayPrediction = "Dead"

    elif TodayPrediction == "Dead":
        TransCondition = np.random.choice(
            TransitionStates[1], replace=True, p=TransitionMatrix[1])

        if TransCondition == "DeDe":
            pass
        
        else:
            TodayPrediction = "Life"
    MarkovChain.append(TodayPrediction)
    print(TodayPrediction)

plt.plot(MarkovChain)
plt.show()
plt.figure()
plt.hist(MarkovChain)
plt.show()