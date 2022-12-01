import numpy as np
from sklearn.model_selection import KFold

StartedData = np.arange(10, 110, 2)
print(f'Started Data: {StartedData} \n +'
      f'Starting Data Length: {len(StartedData)}')

KFold = KFold(n_splits=5, shuffle=True, random_state=1)
fold = 1
for TrainData, TestData in KFold.split(StartedData):
    print(
        '-'*80 + '\n'
        f'Fold: {fold}\n' +
        f'Trainig Data: {StartedData[TrainData]}\n'+
        f'Testing Data: {StartedData[TestData]}\n'

    )
    fold +=1