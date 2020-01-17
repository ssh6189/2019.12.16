import numpy as np

a = np.random.randint(1, 10, (2, 6))
print(a)
a.resize((6, 2))
print(a)
a = np.random.randint(1, 10, (2, 6))
print(a)
a = np.random.randint(1, 10, (2, 6))
print(a)
a.resize((3, 3)) #요소 12개에서 9개로 줄임, 이전 데이터 삭제
print(a)
