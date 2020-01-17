import numpy as np
import random

name = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will','Joe', 'Joe'])

data = np.random.randn(7, 4)

mask = (name == 'bob')|(name =='Will')

print(data[mask])

data[name!='Joe'] = 7

print(data)
