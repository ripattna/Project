while True:
    try :
        a=input(' a :')
        b=input(' b :')
        c=a/b
        print x
        print c
        break
    except (ZeroDivisionError,TypeError, NameError):
        print ' div by zero or type mismath RTE or Name Error'
    except Exception as e:
        print 'unknow err'
        print e
    else:
        print 'no runtime err'
    finally :
        print 'anyway print this'
        
print 'end of pgm'

    
