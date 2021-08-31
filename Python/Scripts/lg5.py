def fn1():
    global a
    a=44
    print 'value of a in fn and addr ' , a, id(a)
   
a=3
print 'value of a in main', a, id(a)
fn1()
print 'value of a back in main', a, id(a)
