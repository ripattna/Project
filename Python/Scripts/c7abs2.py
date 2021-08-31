from abc import ABCMeta, abstractmethod

class Person(object):
    '''Person class for learning'''
    __metaclass__ = ABCMeta
    __n =0
    def __init__(self, name='unk', age=0):
        'this person init learning'
        print 'init '
        self.__name=name
        self.__age=age
        Person.__n+=1

    def __del__(self):
        print 'releasing '
        Person.__n-=1
    def setname(self,name):
        self.__name = name;
    def dispname(self):
        print 'name=',self.__name
    @staticmethod 
    def numemps():
        '''this is static method'''
        print 'num of emps', Person.__n 

    @abstractmethod
    def person_type(self):
        pass

class Emp(Person):
    def __init__(self,name='unk',age=0, salary=1000):
        self.__salary=salary
        Person.__init__(self, name, age)
        
    def getempdetails(self):
        print 'name is : ', self.dispname()
        print 'salary is :', self.__salary
    
    def setsalary(self, salary):
        self.__salary=salary

    def person_type(self):
        return "I am employee"
    
#name mangling p1._Person__age
# object._className__attrName.


#p1=Person() # TypeError: Can't instantiate abstract class Person with abstract methods person_type
#p1.dispname()
e1=Emp()
e1.getempdetails();
print e1.person_type()


          
