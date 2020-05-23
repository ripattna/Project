#do not use this super error 

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

class Emp(Person):
    def __init__(self,name='unk',age=0, salary=1000):
        self.__salary=salary
        super().__init__(self, name, age)
        
    def getempdetails(self):
        print 'details are:', self.dispname(), self.__salary
    def setsalary(self, salary):
        self.__salary=salary
    
#name mangling p1._Person__age
# object._className__attrName.


          
