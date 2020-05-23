import sys
inf=open(sys.argv[1],'r')
outf=open(sys.argv[2],'w')
linecount=charcount=0
for i in inf:
    linecount+=1
    charcount+=len(i)
    outf.write(i)
print ' no of char :', charcount
print ' no of line :', linecount
inf.close()
outf.close()
