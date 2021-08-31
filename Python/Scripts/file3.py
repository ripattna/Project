try :
    fh=open('emp123.txt','r')
    print ' file handle: ', fh
    print ' file name : ',fh.name
    print ' file open mode : ',fh.mode
except IOError as e:
    print ' file not found '
 
except Exception as e:
    print e
print 'End of Program' 
