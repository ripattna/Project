import os.path
if os.path.isfile('D:\pythonpgm\emp.txt') :
    print 'D:\pythonpgm\emp.txt','file exists'
else :
    print 'file does not exists'


if os.path.isfile('D:\pythonpgm\empnothh.txt') :
    print 'file exists'
else :
    print 'D:\pythonpgm\empnothh.txt', 'file does not exists'
