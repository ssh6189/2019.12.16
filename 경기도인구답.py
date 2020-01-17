import numpy as np
import matplotlib as plt
import csv
import pandas

f = open("C:/Users/student/Desktop/경기도인구데이터.csv", "r")

arr = np.load('C:/Users/student/Desktop/경기도인구데이터.csv', delimiter = ',', skiprows = 1, dtype = {'names': ("city", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017"), 'formats':('object', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i')})

#상위 5개 데이터 확인
print(arr[:5])

#배열 크기 확인
print(len(arr))

#배열 크기 확인
print(arr.shape)

#중복 지역 존재 여부 확인
if len(arr['city']) == len(np.unique(arr['city'])):
    print('중복 지역 없음')
else:
    print('중복 지역 있음')

#2017년 수원시 인구 합
import re

char = r'수원시.'

selected_indexes = []

for k in range(len(arr)):
    if re.match(char, arr[k]['city']) != None:
        selected_indexes.append(k)
       
selected_arr = arr[selected_indexes]
suwon_sum = np.sum(selected_arr['2017'])

print('2017년 수원시 총 인구는 %d명'%suwon_sum)

#2017년 인구가 50만 이상인 지역 출력
over_halfM = [arr['city'][k] for k in range(len(arr)) if arr['2017'][k] >= 500000]
print('2017년 인구가 50만 이상인 지역은', over_halfM)


#2017년 경기도 전체 인구의 시별 인구 평균
average17 = np.mean(arr['2017'])
