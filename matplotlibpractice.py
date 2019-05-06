#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np

# Generate data...
x = [2, 3]
y = [2, 5]

# Plot...
plt.scatter(x, y, c=y, s=500)
for i,j in zip(x,y):
    plt.annotate('hello',(i,j))
#plt.gray()

plt.show()
