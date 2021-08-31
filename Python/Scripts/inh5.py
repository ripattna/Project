class A(object):
    def __init__(self):
        print 'init obj of A class'

class B(A):
    def __init__(self):
        super(B,self).__init__()
        print 'init obj of B class'
b=B()


 
