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
class C(B):
    def __init__(self):
        B.__init__(self)
        print 'init obj of C class'
    def disp(self):
        B.disp(self)        
        print 'disp in C class'
c=C()
c.disp()
