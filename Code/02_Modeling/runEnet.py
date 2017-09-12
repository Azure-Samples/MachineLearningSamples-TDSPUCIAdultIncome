# run iris_sklearn.py with descending regularization rates
# run this with just "python run.py". It will fail if you run using az ml execute.

import os
import numpy as np
import math

alphas = []

for p in np.arange(-6,4,1):
    alphas.append(math.pow(2,p))

for alpha in alphas:
    os.system('az ml execute start -c local .\Enet_Hyperparameters.py {}'.format(alpha))