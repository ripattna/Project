import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6]])
print("The Numpy Array:\n", x)
print("Numpy Array shape:", x.shape)
print("Numpy Array size:", x.size)
print("Data Type:", x.dtype)

print("\n#################################\n")


# Creating an Numpy Array with filled zero.
# Return a new array of given shape and type, filled with zeros.
a = np.zeros((3, 4))
print("The Numpy Array:\n", a)
print("Numpy Array size:", a.size)
print("Data Type:", a.dtype)

b = np.arange(10, 19, 2)
print(b)

c = np.linspace(6, 6.3, 6)
print(c)

d = np.full((3, 4), 5)
print(d)

e = np.random.random((3, 4))
print(e)

f = np.arange(24)
print(f)


