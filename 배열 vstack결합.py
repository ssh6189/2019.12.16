import numpy as np

a = np.arange(1, 7).reshape((2, 3))
print(a)
b = np.arange(1, 7).reshape((2, 3))
print(b)

np.vstack((a, b))

#4개 배열을 튜플로 설정
np.vstack((a, b, a, b))
