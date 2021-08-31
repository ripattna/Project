fp=open('emp.txt','r+') # r+ -- read and write - fh -- bof 
#fp.write('end of python classes')
fp.seek(-1,2)
fp.write('\n')
fp.write('end of python classes')
fp.seek(0,0)
print fp.read()
fp.close()
