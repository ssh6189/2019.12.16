import pandas as pd
import numpy as np

dict_data = {'b':2, 'a':1, 'd':np.nan, 'c':3}

sr = pd.Series(dict_data) #1차원 배열, 벡터, label

print(type(sr))
print(pd.isnull(sr))
print(pd.notnull(sr))
print(sr.isnull())
print(sr.notnull())


dict_data2 = {'a':1, 'b':2, 'c':3, 'd':4}
sr2 = pd.Series(dict_data2)
print(sr+sr2)

sr.index.name
