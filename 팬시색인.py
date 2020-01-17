import numpy as np

#NumPy는 불린 인덱싱은 배열 각 요소의 선택 여부를 True, False 지정하는 방식입니다. 
a1 = np.arange(1, 25).reshape((4, 6)) #2차원 배열
print(a1)
# 짝수인 요소 확인
# numpy broadcasting을 이용하여 짝수인 배열 요소 확인
even_arr = a1%2==0
print(even_arr)
# a1[a1%2==0] 동일한 의미입니다. 
a1[even_arr]
np.sum(a1)

print(np.sum(a1))
