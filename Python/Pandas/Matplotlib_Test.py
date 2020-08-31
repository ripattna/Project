import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Defining the dataset
x = np.arange(0, 10, 1)
y = 2*x+5
# Changing the figure
fig = plt.figure(figsize=(10,5))
# Plotting the DataPoints
plt.plot(x, y, linewidth=2.0, linestyle=":", color='r', alpha=0.5, marker='o')
plt.title("Line Plot Demo")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend(['line'], loc='best')
plt.grid(True)
# Plotting the DataPoints
# plt.plot(x,y)
plt.show()

