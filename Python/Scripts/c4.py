class Person:
    n =0
    def __init__(self, name, age):
        #print 'initialising '
        self.__name=name
        self.__age=age
        Person.n+=1
    def __del__(self):
        print 'releasing '
        Person.n-=1
    def setname(self,name):
        self.__name = name;
    def dispname(self):
        print 'name=',self.__name
    @staticmethod 
    def numemps():
        print 'number of emps', Person.n
        print

print Person.numemps() # 0

print 'person.n ---', Person.n

p1=Person('ravi',22)
print Person.numemps()  # 1
p2=Person('san',21)
print Person.numemps() # 2
del p1
print Person.numemps()  # 1
del p2
print Person.numemps()# 0 


          
