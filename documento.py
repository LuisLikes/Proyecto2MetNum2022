from enum import auto
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(auto)
plt.plot(x, x**3 + x**2 + 4, '-b')

plt.show()
