try :
    a=input(' a :')
    b=input(' b :')
    c=a/b
    print c

except TypeError as e:
    print e
    print 'this type err'
    

else:
    print 'no runtime err'
finally :
    print 'anyway print this'


print 'end of pgm'

    
