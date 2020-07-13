import os
f = open("D:/t.txt", 'r')
# print(f.read())
for x in f:
    print(x)
f = open("D:/t1.txt", 'x')
f.close()
os.remove("D:/t1.txt1")
