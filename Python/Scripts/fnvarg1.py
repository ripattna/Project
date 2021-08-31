def fn(*vargs):
    ''' this is an example of fn with variable
        number of parameters '''
    print 'num of parameters passed ',len(vargs)
    for i in vargs:
        print i


# def fn1(): - syntax error - fn should have body - expected an indented block

print fn.__doc__

def fn1():
    pass
 
    
fn(1,2,3,4)
fn('vijay','anand','manju')

fn()


fn1()
