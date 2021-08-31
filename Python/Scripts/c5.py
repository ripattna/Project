class Person:
    __n =0  # n is private - cannot access outside class
    def __init__(self, name, age):
        print 'init '
        self.__name=name
        self.__age=age
        Person.__n+=1
    def __del__(self):
        print 'releasig '
    def setname(self,name):
    #setname method 
        self.__name = name;
    def dispname(self):
        print 'name=',self.__name
    @staticmethod 
    def numemps():
        print 'of of emps', Person.__n 
    
p1=Person('vij',22)
p1.dispname()

Person.numemps()

#print p1.__n # Person instance has no attribute '__n'
#print Person.__n # class Person has no attribute '__n'


          
