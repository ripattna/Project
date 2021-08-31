fh=open('emp.txt','r')
s=fh.readline()
while s:
    print s
    s=fh.readline()
fh.close()
print 'End of Program ' 
