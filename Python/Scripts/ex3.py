while True:
    try :
        a=input(' a :')
        b=input(' b :')
        c=a/b
        print c
        break
    except ZeroDivisionError:
        print 'demon cannot be o'
    except :
        print 'unknow err'
    else:
        print 'no runtime err'
    finally :
        print 'anyway print this'
        
print 'end of pgm'

    
