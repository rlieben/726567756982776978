import numpy as np
import matplotlib.pyplot as plt
from random_generator import *

# Create data


for i in range(MAP['nr_houses'][0]):
    print('x',x)
    print('y',y)
    colors = (0,0,0)
    area = np.pi*3
    plt.scatter(x, y, s=area, c=colors, alpha=0.5)

plt.xlabel('x')
plt.ylabel('y')
plt.show()
