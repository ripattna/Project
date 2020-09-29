# To check the version of the numpy
import numpy as np
import pandas as pd

print("The numpy version is:" + " " + np.__version__)
x = np.arange(1, 10)
print(x)
print(type(x))
y = np.arange(1, 20, 2)
print(y)
z = np.arange(1., 10.)
print(z)

# Test Numpy
data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data)
print(data)
print(s)
