선형대수학

벡터 : 어떤 크기와 방향을 모두 가지는것

스칼라 : 크기만 갖는것

여러개의 정보를 표현할때, 사용하는 벡터는 앞에서 배운 리스트와 비슷하다.

여러개의 데이터를 하나의 정보에 표현한다고 생각할 수 있다.
(*R은 실수를 뜻한다.)

여기까지는 1차원 벡터

행렬 : 벡터가 1개이상 모인것

행과 열로 구성되어, 하나의 정보를 나타내는것

table구조 = matrix구조

사원 table

행단위로 해서 ㅁㅁㅁㅁㅁㅁㅁ
다음과 같이 정보가 구성되어 있다. 사원/이름/급여....
열단위로는 각 직원마다 정보가 있다.

파이썬 스타일 코드로 표현한 벡터

리스트, 튜플, 딕셔너리로 표현이 가능

#데이터에 네이밍을 표시하고 싶다면, 딕셔너리를 쓰자!

벡터의 가장 기본적인 연산은 같은 위치에 있는 값끼리 연산하는것이다.

(a)공식
[a1, a2, a3....] + [b1, b2, b3....] = [a1 + b1, a2 + b2, a3 + b3....]

(b)예시

for i in range(len[u]):
    result.append(
        
numpy를 사용하면, for문을 돌릴 필요가 없다.

def vector_addition(*args):
    return [sum(t) for t in zip(*args)]

vector_addition(u,v,z)
>>[7,10]



간단히 숫자형 변수라고 할 수 있는 스칼라와 벡터는 곱셈연산이 가능하며, 분배법칙을
적용할 수 있다.

a(공식)
a(u+v) = au + av

b(예시)

result = [alpha * sum(t) for t in zip(u,v)]



#여기까지가 벡터와 스칼라 연산
