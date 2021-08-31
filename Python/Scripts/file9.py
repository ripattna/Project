fh=open('empw.txt','a')
#w mode - if file exists - it over writes - otherwise it creates file 
#a mode - if exists opens in append mode - write - writes to end of file
# if file does not exists - it create file 
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


        
