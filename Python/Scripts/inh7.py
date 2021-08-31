class A(object):
    def disp(self):
        print 'disp method of A class'

class B(object):
    def disp(self):
        print 'disp methodof B class'
       
class C(A,B):
    def disp(self):
        super(C,self).disp()
        print 'disp method of C class'
 
c=C()
c.disp()
