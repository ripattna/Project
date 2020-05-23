import sys
print sys.argv
print len(sys.argv) 
for i in sys.argv:
    print i, type(i)
    
s=int(sys.argv[1]) + int(sys.argv[2])
print s
