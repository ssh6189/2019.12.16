import numpy as np

a = np.arange(1, 10).reshape(3,3)
print(a)
#a 배열을 일차원 ㅐ열로 변환하고 1번 index에 99추가
np.insert(a, 1, 999)
#a배열의 axis 0방향 1번 인덱스에 추가
#인덱스가 1인 row에 999가 추가됨
np.insert(a, 1, 999, axis=0)
#a배열의 axis 1방향 1번 인덱스에 추가
#index가 1인 column에 999가 추가됨
np.insert(a, 1, 999, axis=1)
