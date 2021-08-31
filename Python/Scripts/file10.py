fh=open('empw123.txt','a')
#w mode - if file exists - it over writes - otherwise it creates file 
#a mode - if exists opens in append mode - write - writes to end of file
# if file does not exists - it creates file 
while True:
    s=raw_input('enter string to write to file - quit to end :')
    if s=='quit':
        break
    fh.write(s)
print 'writing done - read and display'
fh.close()
fh=open('empw123.txt','r')
print fh.read()
fh.close()
print 'End of program'


        
