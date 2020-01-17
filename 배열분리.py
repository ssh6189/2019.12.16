import numpy as np

a =  np.arange(1, 25).reshape((4, 6))
print(a)
result = np.hsplit(a, 2) #수평으로 두 그룹으로 분할하는 함수
print(result)
