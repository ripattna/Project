def fn1(a):
    " learning fun" 
    print a, id(a) 
    a=a+1
    print a , id(a) , 'in side fn'
    print x


x=10
print x, id(x) 
fn1(x)
print x, id (x) 
#print a - error a has local scope 
