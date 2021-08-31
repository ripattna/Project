fh=open('emp.txt','r')
print 'read output '
print fh.read()
fh.close()

print 
print 'readline output'

fh=open('emp.txt','r')
print fh.readline()
fh.close()
print 
print 'readlines output'

fh=open('emp.txt','r')
print fh.readlines()
fh.close()

