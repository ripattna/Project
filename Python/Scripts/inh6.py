class A(object):
    def disp(self):
        print 'init obj of A class'

class B(A):
    def disp(self):
        super(B,self).disp()
        print 'init obj of B class'
       
b=B()
b.disp()
 
