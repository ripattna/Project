class Person:
    n =10
    def __init__(self, name, age):
        print 'init '
        self.__name=name
        self.__age=age
    def __del__(self):
        print 'releasig '
    def setname(self,name):
        self.__name = name;
    def dispname(self):
        print 'name is',self.__name
    #@staticmethod 
    def wel():
        print 'welcome to person class'
 
        
p1=Person('vijay',33)
print dir(Person)
print dir(p1)
print Person.n  # pl note n is public hence accessible outside class
print p1.n
# print p1.wel() #TypeError: wel() takes no arguments (1 given)
print Person.wel() #method wel() must be called with Person instance as first argument

#print p1.__name__ #AttributeError: Person instance has no attribute '__name__'
print p1._Person__name # name mangling 
 
    


          
