import os
f = open("C:/t.txt", 'r')
# print(f.read())
for x in f:
    print(x)
f = open("C:/t1.txt", 'x')
f.close()
os.remove("C:/t1.txt1")
