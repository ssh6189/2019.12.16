import numpy as np
mean = 0
std = 1
a = np.random.normal(mean, std, (2, 3))
print(a)
data = np.random.normal(0, 1, 10000)
import matplotlib.pyplot as plt
plt.hist(data, bins=100)
plt.show()

a = np.random.rand(3,2)
print(a)
data = np.random.rand(10000)
import matplotlib.pyplot as plt
plt.hist(data, bins=10)
plt.show()

a = np.random.randn(2, 4)
print(a)
data = np.random.randn(10000)
import matplotlib.pyplot as plt
plt.hist(data, bins=10)
plt.show()
