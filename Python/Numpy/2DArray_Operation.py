import numpy as np
x=np.array([5, 10])
print("The value of X", x)
y=np.array([6, 11])
print("The value of Y is:", y)
print(np.sum([[x], [y]], axis=0))
print(np.subtract(x, y))
print(np.equal(x, y))