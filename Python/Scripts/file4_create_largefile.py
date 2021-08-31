fh=open('largefile.txt','r')
print 'read output '
s=fh.read()
print s
fh.close()

print 
print 'open in append mode'

fh=open('largefile.txt','a')
for i in range(20000):
    fh.write(s)
fh.close()

fh=open('largefile.txt','r')
print 'read output '
print fh.read()
fh.close()
