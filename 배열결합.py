import numpy as np

a = np.arange(1, 7).reshape((2,3))
print(a)
b = np.arange(7, 13).reshape((2,3))
print(b)
#axis=0 방향으로 두 배열 결합, axis 기본값 = 0
result = np.concatenate((a, b))
result
#axis=0 방향으로 두 배열 결합, 결과 동일
result = np.concatenate((a, b), axis = 0)
result
#axis=1 방향으로 두 배열 결합, 결과 동일
result = np.concatenate((a, b), axis = 1)
result
