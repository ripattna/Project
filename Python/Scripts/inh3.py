class A(object):
    def __init__(self):
        print 'init obj of A class'
    def disp(self):
        print 'disp in A class'

class B:
    def __init__(self):
        print 'init obj of B class'
    def disp(self):
        print 'disp in B class'
        
class C(A,B):
    def __init__(self):
        super(C,self).__init__()
        print 'init obj of C class'
    def disp(self):
        super(C,self).disp()        
        print 'disp in C class'
c=C()
print c.disp()
