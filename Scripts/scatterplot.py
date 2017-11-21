# Group:        726567756982776978
# Assignment:   Amstelhaege

import numpy as np
import matplotlib.pyplot as plt
from random_generator import *

# Create data

sample = create_test()

for i in range(MAP['nr_houses'][0]):
    x = sample.houses[i].location['x']
    print('x',x)
    y = sample.houses[i].location['y']
    print('y',y)
    colors = (0,0,0)
    area = np.pi*3
    # ax.annotate(data.houses[i].house_id, (x,y))
    plt.scatter(x, y, s=area, c=colors, alpha=0.5)

plt.title('scatterplot for houses')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
