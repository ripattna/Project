class S(object):
    def __init__(self):
        super(S,self).__init__()
        print 'init obj of S class'

class A(S):
    def __init__(self):
        super(A,self).__init__()
        print 'init obj of A class'


class B(S):
    def __init__(self):
        super(B,self).__init__()
        print 'init obj of B class'


       
class C(A,B):
    def __init__(self):
        super(C,self).__init__()
        print 'init obj of C class'

# MRO right to left - depth first 
c=C()
