fh=open('empw.txt','w')
#w mode - if file exists - it over writes - otherwise creates file 
while True:
    s=raw_input('enter string to write to file - quit to end :')
    if s=='quit':
        break
    fh.write(s)
    fh.write('\n')
print 'writing done - read and display'
fh.close()
fh=open('empw.txt','r')
print fh.read()
fh.close()
print 'End of program'


        
