class Person:
    ''' this is person class for learning purpose'''
    def __init__(self, name, age):
        ''' this is constructor '''
        print 'initialising object'
        self.name=name
        self.age=age
    def __del__(self):
        print 'releasing object'
    def setname(self,name):
        self.name = name;
    def dispname(self):
        print 'name is',self.name
    def __str__(self):
        return 'object with name '+self.name 
        
p1=Person('anand',33)  #  __init__(p1,'anand',33)
p1.dispname()
del p1 
p2=Person('vijay',44)
print p2 # special method gets exec implicitly 

#Instead of using the normal statements to access attributes, 
#you can use the following functions          

print hasattr(p2, 'name')    
print getattr(p2, 'name')    
setattr(p2, 'name', 'san')
print getattr(p2, 'name')

#Every Python class keeps following built-in attributes and they can be accessed
# using dot operator like any other attribute

  
print "Person.__doc__:", Person.__doc__
print "Person.__name__:", Person.__name__
print "Person.__module__:", Person.__module__
print "Person.__bases__:", Person.__bases__
print "Person.__dict__:", Person.__dict__
