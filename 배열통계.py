import numpy as np

a = np.arange(1, 10).reshape(3, 3)
print(a)
# np.sum(): 합계
a.sum(), np.sum(a)
a.sum(axis=0), np.sum(a, axis=0)
a.sum(axis=1), np.sum(a, axis=1)
print(a.sum())
 
# np.cumsum(): 누적 합계
a.cumsum(), np.cumsum(a)
a.cumsum(axis=0), np.cumsum(a, axis=0)
a.cumsum(axis=1), np.cumsum(a, axis=1)
print(a.cumsum())

# np.mean(): 평균
a.mean(), np.mean(a)
a.mean(axis=0), np.mean(a, axis=0)
a.mean(axis=1), np.mean(a, axis=1)
print(a.mean())

#np.median(): 중앙값
np.median(a)
np.mean(a, axis=0)
np.mean(a, axis=1)
print(a.median())

# np.corrcoef(): 상관계수
np.corrcoef(a)
print(a.corrcoef())

#np.std(): 표준편차
a.std(), np.std(a)
a.std(axis=0), np.std(a, axis=0)
a.std(axis=1), np.std(a, axis=1)
print(std.corrcoef())
