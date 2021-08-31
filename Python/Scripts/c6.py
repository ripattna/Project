class Person:
    'Person class for learning'
    __n =0
    def __init__(self, name='unk', age=0):
        'this person init learning'
        print 'init '
        self.__name=name
        self.__age=age
        Person.__n+=1
    def __del__(self):
        print 'releasig '
        Person.__n-=1
    def setname(self,name):
    #setname method 
        self.__name = name;
    def dispname(self):
        print 'name=',self.__name
    @staticmethod 
    def numemps():
        'this is static method'
        print 'num of emps', Person.__n 

p1=Person();
p2=Person('vijay')
p3=Person('anand',33)
p4=Person(age=22)


#name mangling p1._Person__age
# object._className__attrName.


          
