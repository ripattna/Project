'''x = lambda x : x + 10
print(x(5))'''

x = lambda x : (x[1], x[0])
print(x(1))

map(lambda x: (x[1], x[0]))