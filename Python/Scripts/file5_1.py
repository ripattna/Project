fh=open('emp.txt','r')
#lst=fh.readlines() - not required 
for i in fh: 
    print i
fh.close()

