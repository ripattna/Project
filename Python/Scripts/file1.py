fh=open('emp.txt','r')
print ' file handle: ', fh
print ' file name : ',fh.name
print ' file open mode : ',fh.mode
print ' file open mode : ',fh.closed
fh.close()
print ' file open mode : ',fh.closed

