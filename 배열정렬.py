import numpy as np
#ndarray 객체는 axis를 기준으로 요소 정렬하는 sort 함수를 제공합니다.
unsorted_arr = np.random.random((3, 3))
print(unsorted_arr)
#데모를 위한 배열 복사
unsorted_arr1 = unsorted_arr.copy()
unsorted_arr2 = unsorted_arr.copy()
unsorted_arr3 = unsorted_arr.copy()

unsorted_arr1.sort()  #배열 정렬
print(unsorted_arr1)

unsorted_arr2.sort(axis=0)   #배열 정렬, axis=0
print(unsorted_arr2)

unsorted_arr3.sort(axis=1) #배열 정렬, axis=1
print(unsorted_arr3)

