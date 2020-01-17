import numpy as np

a =  np.random.randint(1, 10, (2, 3))

print(a)
a.ravel()
b=a.ravel()
print(b)
b[0] = 99
print(b)
print(a)

a =  np.random.randint(1, 10, (2, 3))
print(a)

result = a.reshape((3, 2, 1))
print(result)
