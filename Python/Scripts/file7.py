fh=open('emp.txt','r')
print 'file ptr position :', fh.tell()
print ' 1st 15 char :', fh.read(15)
print 'file ptr position :', fh.tell()

fh.seek(-9,2)

#fh.seek(30,0)  --> move fp 30 bytes from  bof
#fh.seek(-  + 22,1) --> move fp 22 bytes from current pos
#fh.seek(-10,2)  --> move fp 30 bytes from  bof

print ' last 9 char :' ,fh.read(9)
#fh.seek(bytes, ref - 0 begin, 1 current, 2 end
fh.close()
print 'End of Program ' 
