numpy

numpy는 내부적으로 데이터를 다른 내장 파이썬 객체와 구분된 연속된 메모리 블록에 저장한다.

numpy의 각종 알고리즘은 모두 C로 작성되어 타입검사나 다른 오버헤드 없이
메모리를 직접 조작할 수 있다.

Numpy 연산은 파이썬 반복문을 사용하지 않고, 전체 배열에 대한 복잡한 계산을 수행할 수 있다.

Numpy를 사용한 코드가 순수 파이썬으로 작성한 코드보다 훨씬 빠르며, 메모리도 적게 사용한다.


ndarray객체 생성법

np.arange()
np.random.rand(x, y)

ndtype, nshape, ndim

8bit면

맨 앞은 sign비트

즉, int8이라고 하면, -128 ~ 127까지 저장하는 비트

16bit는

-(2^15) ~ (2^15-1)



astype : 형변환함수

형변환과 배열 객체에 대한 벡터계산 알기



난수기반 배열생성

np.random.normal함수

np.random.rand 함수

np.random.randn함수

np.random.randint함수

np.random.random함수



브로드캐스팅
차원이 다른애들을 연산할 수 있도록 변환



색인과 슬라이싱

numpy의 배열 색인에 대해서는 다룰 주제가 많다. 데이터의 부분집하비나 개별요소를
선택하기 위한 수많은 방법이 존재한다.

[1, 2, 3, 4, 5, 6, 7, 8, 9]
list와의 차이는 만약 [5:8]를 색인시 그냥, [5, 6, 7]로 보여지는것은 뷰만보여진다.

새로 객체가 생기는것이 아니다.

1차원 배열
[idx]

2차원 배열
[idx][jdx] 행선택
만약 하나만 오면, 행에대한 인덱스

!=, ~= not 연산자

벡터연산 지원

일일이 하나씩 하는것보다 100배 이상 빠르다.

#머신러닝에서 선형대수 연산을 처리할때 매우 도움이 된다.

ndarray 배열 객체에 대한 slice, subset, indexing이 반환하는 배열은 새로운 객체가 아닌
기존 배열의 뷰이다.

ndarray객체는  axis를 기준으로 요소정렬하는 sort함수를 제공한다.

0:행
1:렬

.
.
.
.

아무것도 지정 안하면, 행기준이다.

numpy 서브셋, 슬라이싱, 인덱싱

Numpy는 불린 인덱싱은 배열 각 요소의 선택여부를 True, False를 지정하는 방식
해당 인덱스의 True만을 조회한다.

팬시 인덱싱
배열에 인덱스배열을 전달하여 요소를 참조하는 방법

arr=np.range.reshape((4,6))
print(arr)

[arr[0,0], arrp1,1], arr[2,2], ar[3,3]]

arr[[0,1,2,3], [0,1,2,3]]

arr[:, [1,2]]

팬시색인은 슬라이싱과는 달리 선택된 데이터를 새로운 데이터로 복사한다.

import numpy as np

arr = np.arange(32).reshape((8, 4))

arr

arr[[1,5,7,2], [0,3,1,2]]

그러면, 결과는 array([4, 23, 29, 10])

1행 0열, 5행 3열.... 이런식이다.

새로운 배열을 리턴한다.

#즉, 팬시색인은 깊은 복사이다.

3차원
axis = 0 : 면
axis = 1 : 행
axis = 2 : 열

a1 = np.arange(27).reshape(3,3,3)
print(a)
a.sum(axis=0) #면
a.sum(axis=1) #행
a.sum(axis=2) #열

유니버셜함수 : 배열의 각 원소를 빠르게 처리하는 함수

sqrt, exp : 단항 유니버셜함수
add, maximum : 이항 유니버셜함수

Numpy 입출력
np.save()
np.savez()
np.load()
np.loadtxt()
np.savetxt()

np.save, np.load는 pickle의 dump와 load와 비슷하다.

reshape는 데이터 변경없이 지정된 shape로 변환하는 메서드
실제 데이터를 변경하는게 아니라, 형태만 바꿔서, 뷰만 리턴한다.

ravel 함수 : 배열의 shape를 1차원 배열로 만드는 메서드, numpy.ndarray 배열 객체의 view 반환
ravel매서드가 반환하는 배열은 원본 배열이 뷰
ravel 메서드가 반혼하는 배열의 요소를 수정하면, 원본 배열 요소에도 반영

resize() 함수 : 배열의 shape와 크기 변경
np.resize(a, new_shape) : shape와 요소 다바뀐다.
np.ndarray.resize(new_shape, refcheck=True)
np.resize와 np.reshape 함수는 배열의 shape를 변경한다는 부분에서 유사하다.
차이점은 reshape 함수는 배열 요소 수를 변경하지 않는다.
reshape 전후 배열의 요소 수는 같습니다.
resize는 shape를 변경한느 과정에서 배열 요소 수를 줄이거나, 늘립니다.
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



append() 함수 : 배열의 끝에 값을 추가
np.append(arr, values, axis=None)
arr의 끝에 values(배열)을 추가합니다.
axis로 배열이 추가되는 방향을 지정할 수 있습니다.

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


배열 요소 추가 삭제
insert(): axis를 지정하지 않으며, 1차원 배열로 변환
np.insert(arr, obj, values, axis=None)
추가할 방향을 axis로 지정

a = np.arange(1, 10).reshape(3,3)
print(a)
a 배열을 일차원 배열로 변환하고 1번 index에 99추가
np.insert(a, 1, 999)
#a배열의 axis 0방향 1번 인덱스에 추가
#인덱스가 1인 row에 999가 추가됨
np.insert(a, 1, 999, axis=0)
#a배열의 axis 1방향 1번 인덱스에 추가
#index가 1인 column에 999가 추가됨
np.insert(a, 1, 999, axis=1)

delete() : 원본 배열을 변경하지 않으며, 새로운 배열을 반환
np.delete(arr, obj, axis=None)
axis를 지정하지 않으며, 1차원 배열로 변환
삭제할 방향을 axis로 지정

a = np.arange(1, 10).reshape(3, 3)
print(a)
# a 배열을 일차원 배열로 변환하고 1번 index 삭제
np.delete(a, 1)
# a 배열의 axis 0방향 1번 인덱스인 행을 삭제한 배열을 생성하여 반환
np.delete(a, 1, axis=0)
# a 배열의 axis 1방향 1번 인덱스인 열을 삭제한 배열을 생성하여 반환
np.delete(a, 1, axis=1)

배열 결합
np.concatenate((a1, a2,....), axis=0)

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



배열결합
np.vstack(tup):수직방향 배열 결합
tup: 튜플
튜플로 설정된 여러 배열을 수직방향으로 여결 (axis=0 방향)
np.concatenate(tup, axis=0)과 동일

a = np.arange(1, 7).reshape((2, 3))
print(a)
b = np.arange(1, 7).reshape((2, 3))
print(b)

np.vstack((a, b))

#4개 배열을 튜플로 설정
np.vstack((a, b, a, b))

#hstack도 동일

배열 분리

numpy는 배열을 수직, 수평으로 분할하는 함수를 제공합니다.
np.hsplit(ary, indices_or_sections) : 지정한 수평(행) 방향으로 분할
np.vsplit():지정한 배열을 수직(열) 방향으로 분할

a =  np.arange(1, 25).reshape((4, 6))
print(a)
result = np.hsplit(a, 2) #수평으로 두 그룹으로 분할하는 함수
print(result)

배열 분리 : 수평방향으로 여러구간으로 구분 - np.hsplit으 두번째 파라미터에 구간 설정 배열을 전달
하여 여러배열로 구분합니다.

np.hsplit(a, [1, 3, 5])

np.vsplit(ary, indices_or_sections) : 배열을 수직방향(행방향)으로 분할하는 함수

result = np.vsplit(a, 4)
result
np.array(result).shape

np.hsplit의 두번째 파라미터에 구간 설정 배열을 전달하여 여러 배열로 구분

#수직 방향으로 여러구간으로 구분
result = np.vsplit(a, [1, 3]) #row를 1, 2~3, 4번째 라인으로 구분
result
np.array(result).shape
