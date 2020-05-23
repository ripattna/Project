import sys
try :
    print sys.argv
    for i in sys.argv:
        print i, type(i)
    
    s=int(sys.argv[1]) + int(sys.argv[2])
    print s
except IndexError:
    print ' pass 2 nos'
print 'endo of program' 
