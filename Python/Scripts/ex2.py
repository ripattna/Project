try :
    a=input(' a :')
    b=input(' b :')
    c=a/b
    print c
except ZeroDivisionError as e:
    print 'demon cannot be 0 zero'
    print e
    print type(e)
except TypeError as e:
    print e
    print 'this type err'
    
except Exception as e:
    print 'unknow err'
    print e
    print type(e)
else:
    print 'no runtime err'
finally :
    print 'anyway print this'
    print e


print 'end of pgm'

    
