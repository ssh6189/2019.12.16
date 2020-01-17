import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(0, 1, 5)
plt.plot(a, 'o')
plt.show()

a = np.arange(0, 10, 2, np.float)
plt.plot(a, 'o')
plt.show()

a = np.logspace(0.1, 1, 20, endpoint=True)
plt.plot(a, 'o')
plt.show()
