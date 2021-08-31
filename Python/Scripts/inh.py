class A:
    def __init__(self):
        print 'init obj of A class'
    def disp(self):
        print 'disp in A class'
class B(A):
    def __init__(self):
        A.__init__(self)
        print 'init obj of B class'
    def disp(self):
        A.disp(self)        
        print 'disp in B class'

b=B();
b.disp()

