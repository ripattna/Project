import numpy as np

x = np.arange(1, 11)
print('X :', x)
print("x size:", x.size)
print("x shape:", x.shape)
print("X Dimension:", x.ndim)

a = x.reshape(5, 2)
print(a)
print("A size:", a.size)
print("A shape:", a.shape)
print("A Dimension:", a.ndim)

r = np.arange(1, 10).reshape(3, 3)
print(r)

