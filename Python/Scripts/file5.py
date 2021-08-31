fh=open('emp.txt','r')
lst=fh.readlines()
for i in lst:
    print i

print
print

for i in range(len(lst)):
    print lst[i]

fh.close()

