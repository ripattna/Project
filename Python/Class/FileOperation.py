import os
f = open("C:/tmp/t.txt", 'r')
print(f.read())
for x in f:
    print(x)
# f = open("C:/tmp/t1.txt", 'x')
# f.close()
# os.remove("C:/tmp/t1.txt1")
