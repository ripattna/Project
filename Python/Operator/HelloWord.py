print("\n",
  """      | |
      -----
       | |
      -----
       | |""")

x = ("appple","banana","mango")
a = ("rissan",)
y = list(x)
print(type(x))
print(type(y))
y[1] = "orange"
x = tuple(y)
print(x)
print(type(a))