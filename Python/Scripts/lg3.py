def fn1():
    a = 2
    global a=a+10 
a=20
print a
fn1()
print a
#error 
