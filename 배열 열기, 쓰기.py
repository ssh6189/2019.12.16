import numpy as np

a = np.random.randint(0, 10, (2, 3))
b = np.random.randint(0, 10, (2, 3))

#print(a)
#print(b)

# a배열 파일에 저장
np.save("./my_array1", a)
# a, b 두 개 배열을 파일에 저장
np.savez("my_array2", a, b)

print(np.load("C:/Users/student/Desktop/my_array1.npy"))

npzfiles = np.load("C:/Users/student/Desktop/my_array2.npz")

print(npzfiles['arr_0'])
print(npzfiles['arr_1'])

