import numpy as np

a = np.arange(1, 10).reshape(3, 3)
print(a)
# a 배열을 일차원 배열로 변환하고 1번 index 삭제
np.delete(a, 1)
# a 배열의 axis 0방향 1번 인덱스인 행을 삭제한 배열을 생성하여 반환
np.delete(a, 1, axis=0)
# a 배열의 axis 1방향 1번 인덱스인 열을 삭제한 배열을 생성하여 반환
np.delete(a, 1, axis=1)
