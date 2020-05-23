i=1
while i <=3:
    try :
        a=input(' a :')
        b=input(' b :')
        c=a/b
        print c
        break
    except ZeroDivisionError:
        print 'demon cannot be o'
        i=i+1
    except :
        print 'unknow err'
    else:
        print 'no runtime err'
    finally :
        print 'anyway print this'
        
print 'end of pgm'

    
