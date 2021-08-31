class Person:
    n =10
    def __init__(self, name, age):
        print 'init '
        self.__name=name  # private inst var 
        self.__age=age
    def __del__(self):
        print 'releasig '
    def setname(self,name):
        self.__name = name;
    def dispname(self):
        print 'name is',self.__name
    @staticmethod 
    def wel():
        print 'welcome to person class'
 
        
p1=Person('vijay',33)
print p1.dispname()
print dir(Person)
print dir(p1)
print Person.n

print Person.wel()

print p1.__name #AttributeError: Person instance has no attribute '__name__'

#print hasattr(p1, '__name')  error  
#print getattr(p1, '__name')    
#setattr(p1, '__name', 'san')
#print getattr(p1, '__name')


#print p1._Person__name # name mangling 
 
    


          
