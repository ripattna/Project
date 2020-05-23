class A(object):
    def __init__(self):
        super(A,self).__init__()
        print 'init obj of A class'


class B(object):
    def __init__(self):
        super(B,self).__init__()
        print 'init obj of B class'


       
class C(B,A):
    def __init__(self):
        super(C,self).__init__()
        print 'init obj of C class'


# MRO right to left and then child i.e. current 
