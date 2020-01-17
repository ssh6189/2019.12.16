import numpy as np

a = np.arange(1,10).reshape(3,3)
print(a)
b = np.arange(10, 19).reshape(3,3)
print(b)
#axis 지정없이 추가, 배열은 1차원 배열로 변형되어 결합됩니다.
result = np.append(a, b)
print(result)
print(a)#원본 배열을 변경하는것이 아니며, 새로운 배열이 생성됩니다.
#axis 방향으로 b배열 추가
result = np.append(a, b, axis=0)
print(result)
#axis = 0 설정시, shape[0]을 제외한 나머지 shape는 같아야 한다.
#shape[0]을 제외한 나머지 shape가 다를경우 append는 오류 발생
different_shape_arr = np.arange(10, 20).reshape(2,5)
print(different_shape_arr)
#기준 축을 제외한 shape가 다른 배열의 appnd: 오류 발생
np.append(a, different_shape_arr,axis=0)
